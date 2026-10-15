#!/usr/bin/env python3
"""Generate a small update feed from already published, verified Release assets.
Fetch assets with gh release download before running; never publish the feed first.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import struct
import tempfile
import zipfile
from build import require, identity

ROOT = Path(__file__).resolve().parents[1]


def content_hash(root):
    digest = hashlib.sha256()
    for path in sorted(root.rglob('*'), key=lambda p: p.relative_to(root).as_posix().encode()):
        require(not path.is_symlink(), 'symlinks forbidden')
        relative = path.relative_to(root).as_posix().encode()
        digest.update(struct.pack('<Q', len(relative)))
        digest.update(relative)
        digest.update(b'D' if path.is_dir() else b'F')
        if path.is_file():
            digest.update(path.read_bytes())
    return digest.hexdigest()


def generate(assets, tag, previous):
    require(re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+', tag), 'invalid release tag')
    old = {e['identifier']: e for e in previous.get('extensions', [])}
    source = json.loads((assets / 'catalog.json').read_text())
    entries = []
    for item in source['extensions']:
        require(item['status'] == 'verified' and item.get('minimumBubbooVersion'), 'stable verified entries only')
        artifact = item['artifact']
        require(re.fullmatch(r'[A-Za-z0-9._-]+\.popclipextz', artifact), 'unsafe artifact')
        archive = assets / artifact
        data = archive.read_bytes()
        require(len(data) == item['bytes'] and hashlib.sha256(data).hexdigest() == item['sha256'], 'asset checksum mismatch')
        with tempfile.TemporaryDirectory() as tmp:
            with zipfile.ZipFile(archive) as bundle:
                for name in bundle.namelist():
                    path = Path(name)
                    require(not path.is_absolute() and '..' not in path.parts and '\\' not in name, 'unsafe ZIP path')
                bundle.extractall(tmp)
            children = list(Path(tmp).iterdir())
            require(len(children) == 1 and identity(children[0]) == item['identifier'], 'identity mismatch')
            digest = content_hash(children[0])
        history = []
        if item['identifier'] in old:
            prior = old[item['identifier']]
            history = list(prior['history'])
            old_version = tuple(map(int, prior['version'].split('.')))
            new_version = tuple(map(int, item['version'].split('.')))
            require(new_version >= old_version, 'version downgrade')
            if digest != prior['contentSHA256']:
                require(new_version > old_version, 'changed content must increment extension version')
                history.append({'version': prior['version'], 'contentSHA256': prior['contentSHA256']})
            history = [r for r in history if r['contentSHA256'] != digest]
        entries.append({
            'identifier': item['identifier'], 'version': item['version'],
            'minimumBubbooVersion': item['minimumBubbooVersion'],
            'contentSHA256': digest, 'sha256': item['sha256'], 'bytes': item['bytes'],
            'downloadURL': f'https://github.com/Superoutman/Bubboo-Extensions/releases/download/{tag}/{artifact}',
            'history': history
        })
    require(len({e['identifier'] for e in entries}) == len(entries), 'duplicate identifier')
    return {'schemaVersion': 1, 'extensions': entries}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--assets', type=Path, required=True)
    parser.add_argument('--tag', required=True)
    parser.add_argument('--output', type=Path, default=ROOT / 'catalog/updates.json')
    args = parser.parse_args()
    previous = json.loads(args.output.read_text()) if args.output.exists() else {}
    result = generate(args.assets, args.tag, previous)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
    print(f"Generated {len(result['extensions'])} update entries.")
