__author__ = 'Hiroaki'

import unittest
from browserprinter.printer import Configure


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.conf = Configure({
            'top_page': 'http://www.yahoo.co.jp',
            'includes': ['http://docs.yahoo.co.jp', 'https://google.co.jp'],
            'excludes': ['http://docs.yahoo.co.jp/info', 'https://doc.google.co.jp'],
            'dest_dir': 'screenshots',
            'driver': 'Firefox'
        })

    def test_contains_include(self):
        self.assertTrue(self.conf.contains_include('https://google.co.jp'))

    def test_contains_include_false(self):
        self.assertFalse(self.conf.contains_include('http;//google.co.jp'))

    def test_contains_exclude(self):
        self.assertTrue(self.conf.contains_exclude('https://doc.google.co.jp'))
        self.assertTrue(self.conf.contains_exclude('https://doc.google.co.jp/test'))

    def test_contains_exclude_false(self):
        self.assertFalse(self.conf.contains_exclude('http://doc.google.co.jp/test'))


if __name__ == '__main__':
    unittest.main()
