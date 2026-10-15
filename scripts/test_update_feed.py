#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import plistlib
import tempfile
import unittest
import zipfile
from update_feed import generate


class FeedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def asset(self, version='0.1.0', content='first'):
        artifact = 'Test-0.1.0.popclipextz'
        with zipfile.ZipFile(self.root / artifact, 'w') as archive:
            archive.writestr('Test.popclipext/Config.plist', plistlib.dumps({'Extension Identifier': 'test.id'}))
            archive.writestr('Test.popclipext/content.txt', content)
        data = (self.root / artifact).read_bytes()
        (self.root / 'catalog.json').write_text(json.dumps({'extensions': [{
            'identifier': 'test.id', 'version': version, 'status': 'verified',
            'minimumBubbooVersion': '0.1.2', 'artifact': artifact,
            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)
        }]}))

    def test_initial_and_history(self):
        self.asset()
        first = generate(self.root, 'v0.1.1', {})
        self.assertEqual(first['extensions'][0]['history'], [])
        self.asset('0.1.1', 'second')
        second = generate(self.root, 'v0.1.2', first)
        self.assertEqual(second['extensions'][0]['history'], [{
            'version': '0.1.0', 'contentSHA256': first['extensions'][0]['contentSHA256']
        }])

    def test_requires_version_increment(self):
        self.asset()
        first = generate(self.root, 'v0.1.1', {})
        self.asset(content='changed')
        with self.assertRaises(ValueError):
            generate(self.root, 'v0.1.2', first)

    def test_rejects_downgrade_and_corruption(self):
        self.asset('0.2.0')
        first = generate(self.root, 'v0.1.1', {})
        self.asset('0.1.0')
        with self.assertRaises(ValueError):
            generate(self.root, 'v0.1.2', first)
        (self.root / 'Test-0.1.0.popclipextz').write_bytes(b'corrupt')
        with self.assertRaises(ValueError):
            generate(self.root, 'v0.1.2', {})


if __name__ == '__main__':
    unittest.main()
