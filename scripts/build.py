#!/usr/bin/env python3
"""Validate curated original-format packages; build only explicitly verified entries."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import stat
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ('LICENSE.txt', 'NOTICE.md', 'UPSTREAM.json')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def identity(package):
    if (package / 'Config.json').exists():
        return json.loads((package / 'Config.json').read_text())['identifier']
    if (package / 'Config.plist').exists():
        return plistlib.loads((package / 'Config.plist').read_bytes())['Extension Identifier']
    script = package / 'Config.js'
    require(script.is_file(), f'{package.name}: no supported manifest')
    match = re.search(r'^//\s*identifier:\s*(\S+)\s*$', script.read_text(), re.M)
    require(match, f'{package.name}: missing explicit identifier')
    return match.group(1)


def validate(root):
    require(not (root / "extensions").is_symlink(), "extensions root must not be a symlink")
    entries = json.loads((root / 'catalog/entries.json').read_text())
    require(isinstance(entries, list), 'entries must be an array')
    seen_ids, seen_packages = set(), set()
    validated = []
    for entry in entries:
        name, identifier = entry['package'], entry['identifier']
        require(re.fullmatch(r'[A-Za-z0-9_-]+\.popclipext', name), 'unsafe package name')
        require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]+', identifier), 'unsafe identifier')
        require(name not in seen_packages and identifier not in seen_ids, 'duplicate package or identifier')
        seen_packages.add(name); seen_ids.add(identifier)
        require(entry['status'] in ('candidate', 'blocked', 'verified'), 'unknown status')
        require(re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', entry['version']), 'invalid curated version')
        package = root / 'extensions' / name
        require(package.is_dir() and not package.is_symlink(), f'{name}: missing directory or symlink')
        files, total, path_count = [], 0, 0
        seen_paths = set()
        for path in sorted(package.rglob('*')):
            relative = path.relative_to(root / 'extensions').as_posix()
            require(relative.casefold() not in seen_paths, f'{relative}: case-insensitive path collision')
            seen_paths.add(relative.casefold())
            require(not any(ord(char) < 32 or ord(char) == 127 for char in relative), 'control characters in path')
            mode = path.lstat().st_mode
            require(not stat.S_ISLNK(mode), f'{relative}: symlinks forbidden')
            require(stat.S_ISREG(mode) or stat.S_ISDIR(mode), f'{relative}: special file forbidden')
            require('\\' not in relative and len(relative.encode()) <= 512 and all(part not in ('..', '.', '') for part in relative.split('/')), 'unsafe path')
            path_count += 1
            require(path_count <= 512, f'{name}: too many entries')
            if path.is_file():
                data = path.read_bytes()
                require(len(data) <= 16 * 1024 * 1024, f'{relative}: file too large')
                total += len(data)
                files.append((relative, data))
        require(total <= 64 * 1024 * 1024, f'{name}: package too large')
        require(identity(package) == identifier, f'{name}: manifest identifier mismatch')
        for filename in REQUIRED:
            require((package / filename).is_file() and (package / filename).stat().st_size, f'{name}: missing {filename}')
        upstream = json.loads((package / 'UPSTREAM.json').read_text())
        require(upstream.get('author') and upstream.get('repository') and re.fullmatch(r'[0-9a-f]{40}', upstream.get('commit', '')), f'{name}: incomplete upstream provenance')
        require(entry.get('author') == upstream['author'], f'{name}: author differs from provenance')
        require(entry.get('license') == 'MIT', f'{name}: license needs review')
        require('Permission is hereby granted' in (package / 'LICENSE.txt').read_text(), f'{name}: MIT license text missing')
        if entry['status'] == 'verified':
            tested = entry.get('testedBubbooBuild', {})
            exact_development_build = tested.get('channel') == 'development' and re.fullmatch(r'[0-9a-f]{64}', tested.get('executableSHA256', ''))
            require(entry.get('acceptance') and (entry.get('minimumBubbooVersion') or exact_development_build), f'{name}: verified entries require acceptance and a released minimum version or exact development build')
        validated.append((entry, files))
    actual = {p.name for p in (root / 'extensions').iterdir() if p.is_dir() and p.suffix == '.popclipext'}
    require(actual == seen_packages, 'catalog must explicitly account for every extension package')
    return validated


def build(root, output):
    validated = validate(root)
    verified = [(e, f) for e, f in validated if e['status'] == 'verified']
    require(verified, 'No verified entries: no release artifacts produced. Complete acceptance first.')
    require(not output.exists() or not any(output.iterdir()), 'output directory must be absent or empty; prevents stale artifacts')
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='bubboo-release-', dir=output.parent) as temporary:
        staging = Path(temporary)
        catalog, checksums = [], []
        for entry, files in sorted(verified, key=lambda item: item[0]['identifier']):
            filename = f"{entry['package'][:-11]}-{entry['version']}.popclipextz"
            archive = staging / filename
            with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_STORED, allowZip64=False) as bundle:
                for name, data in files:
                    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                    info.create_system = 3
                    info.external_attr = (stat.S_IFREG | 0o644) << 16
                    bundle.writestr(info, data)
            require(archive.stat().st_size <= 64 * 1024 * 1024, 'archive too large')
            digest = hashlib.sha256(archive.read_bytes()).hexdigest()
            checksums.append(f'{digest}  {filename}')
            catalog.append(dict(entry, artifact=filename, sha256=digest, bytes=archive.stat().st_size, format='popclip'))
        catalog_file = staging / 'catalog.json'
        catalog_file.write_text(json.dumps({'schemaVersion': 1, 'extensions': catalog}, indent=2, ensure_ascii=False) + '\n')
        checksums.append(f"{hashlib.sha256(catalog_file.read_bytes()).hexdigest()}  catalog.json")
        (staging / 'SHA256SUMS').write_text('\n'.join(checksums) + '\n')
        output.mkdir(exist_ok=True)
        for file in staging.iterdir():
            os.replace(file, output / file.name)
    return len(verified)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='validate all entries without producing artifacts')
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    try:
        if args.check:
            values = validate(ROOT)
            print(f'Validated {len(values)} entries; {sum(e["status"] == "verified" for e, _ in values)} verified.')
        else:
            print(f'Built {build(ROOT, args.output.resolve())} verified packages.')
    except (ValueError, KeyError, OSError, json.JSONDecodeError, plistlib.InvalidFileException) as error:
        parser.exit(1, f'Error: {error}\n')
