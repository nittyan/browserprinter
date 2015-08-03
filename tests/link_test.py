# -*- coding:utf-8 -*-

import unittest
from browserprinter.printer import Link


class LinkTestCase(unittest.TestCase):

    def setUp(self):
        self.includes = ['https://google.co.jp']
        self.excludes = ['https://docs.google.co.jp', 'https://google.co.jp/sample']

    def tearDown(self):
        pass

    def test_invalid_scheme(self):
        link = Link('htt://www.google.co.jp')
        self.assertFalse(link.is_valid())

    def test_file_scheme(self):
        link = Link('file://www.google.co.jp')
        self.assertFalse(link.is_valid())

    def test_fragmented_scheme(self):
        link = Link('http;//www.google.co.jp/test#aaa')
        self.assertFalse(link.is_valid())

    def test_none(self):
        link = Link(None)
        self.assertFalse(link.is_valid())

    def test_valid_url(self):
        link = Link('http://www.google.co.jp/test')
        self.assertTrue(link.is_valid())

    def test_eq_none(self):
        self.assertFalse(Link('http://www.google.co.jp') == None)

    def test_eq(self):
        self.assertTrue(Link('http://www.google.co.jp') == Link('http://www.google.co.jp'))

    def test_is_includes(self):
        self.assertTrue(Link('https://google.co.jp/test')._is_includes(self.includes))

    def test_is_excludes(self):
        self.assertTrue(Link('https://docs.google.co.jp/test')._is_excludes(self.excludes))

    def test_do_crawl_true(self):
        self.assertTrue(Link('https://google.co.jp/test').do_crawl(self.includes, self.excludes))

    def test_do_crawl_false(self):
        self.assertFalse(Link('https://google.co.jp/sample/main').do_crawl(self.includes, self.excludes))


if __name__ == '__main__':
    unittest.main()
