# -*- coding:utf-8 -*-

import unittest
from unittest.mock import Mock, patch
from browserprinter.printer import BrowserPrinter, Configure
import requests


class BrowserPrinterTestCase(unittest.TestCase):

    def setUp(self):
        self.config = Configure({
            'top_page': 'http://www.yahoo.co.jp',
            'includes': ['http://docs.yahoo.co.jp'],
            'excludes': ['http://docs.yahoo.co.jp/info'],
            'dest_dir': 'screenshots',
            'driver': 'Firefox'
        })

    def test_did_crawl(self):
        printer = BrowserPrinter(self.config)
        self.assertTrue(printer.did_crawl('https://test', ['https://test', 'http;//test']))

    def test_did_crawl_false(self):
        printer = BrowserPrinter(self.config)
        self.assertFalse(printer.did_crawl('http://test', ['http://ttest']))

    def test_do_crawl(self):
        printer = BrowserPrinter(self.config)
        self.assertTrue(printer.do_crawl('http://docs.yahoo.co.jp/test', []))

    def test_do_crawl_false(self):
        printer = BrowserPrinter(self.config)
        self.assertFalse(printer.do_crawl('https://test', []))

    def test_find_link(self):
        requests.get = Mock()

        class Temp(object):
            text = """
              <html><a href= "http://docs.yahoo.co.jp/target"></a></html>
            """
        requests.get.return_value = Temp()
        printer = BrowserPrinter(self.config)

        self.assertEqual(['http://docs.yahoo.co.jp/target'], printer.find_link('top'))

    # def test_browserprinter(self):
    #     config = Configure({
    #         'top_page': 'http://www.yahoo.co.jp',
    #         'includes': ['http://docs.yahoo.co.jp'],
    #         'excludes': ['http://docs.yahoo.co.jp/info'],
    #         'dest_dir': 'screenshots',
    #         'driver': 'Firefox'
    #     })
    #
    #     printer = BrowserPrinter(config)
    #     printer.execute()


if __name__ == '__main__':
    unittest.main()
