"""Isolated release-gate regression tests. Never changes curated source packages."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location('build', Path(__file__).with_name('build.py'))
build = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build)


class ReleaseGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(build.ROOT / 'extensions', self.root / 'extensions')
        shutil.copytree(build.ROOT / 'catalog', self.root / 'catalog')
        # Deliberately reset copied states; tests remain valid after real acceptance updates.
        entries = self.entries()
        for entry in entries:
            entry['status'] = 'candidate'
        self.save(entries)

    def tearDown(self):
        self.temp.cleanup()

    def entries(self):
        return json.loads((self.root / 'catalog/entries.json').read_text())

    def save(self, entries):
        (self.root / 'catalog/entries.json').write_text(json.dumps(entries))

    def test_no_verified_means_no_artifacts(self):
        output = self.root / 'dist'
        with self.assertRaisesRegex(ValueError, 'No verified'):
            build.build(self.root, output)
        self.assertFalse(output.exists())

    def test_deterministic_archives_and_only_verified(self):
        entries = self.entries()
        entries[0].update(status='verified', acceptance='test fixture only', minimumBubbooVersion='0.0.0')
        self.save(entries)
        a, b = self.root / 'a', self.root / 'b'
        self.assertEqual(build.build(self.root, a), 1)
        self.assertEqual(build.build(self.root, b), 1)
        self.assertEqual({p.name: p.read_bytes() for p in a.iterdir()}, {p.name: p.read_bytes() for p in b.iterdir()})
        archive = next(a.glob('*.popclipextz'))
        with build.zipfile.ZipFile(archive) as bundle:
            for required in build.REQUIRED:
                self.assertIn(f"{entries[0]['package']}/{required}", bundle.namelist())
        with self.assertRaisesRegex(ValueError, 'output directory'):
            build.build(self.root, a)

    def test_manifest_mismatch_and_traversal_rejected(self):
        entries = self.entries()
        entries[0]['identifier'] = 'com.example.wrong'
        self.save(entries)
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            build.validate(self.root)
        entries[0]['package'] = '../Escape.popclipext'
        self.save(entries)
        with self.assertRaisesRegex(ValueError, 'unsafe package'):
            build.validate(self.root)

    def test_symlinks_and_missing_license_rejected(self):
        package = self.root / 'extensions' / self.entries()[0]['package']
        link = package / 'link'
        link.symlink_to('/etc/passwd')
        with self.assertRaisesRegex(ValueError, 'symlinks'):
            build.validate(self.root)
        link.unlink()
        (package / 'LICENSE.txt').unlink()
        with self.assertRaisesRegex(ValueError, 'missing LICENSE'):
            build.validate(self.root)


if __name__ == '__main__':
    unittest.main()
