# -*- coding:utf-8 -*-

import unittest
from unittest.mock import Mock, patch, MagicMock
from browserprinter.printer import BrowserPrinter, Configure, Link
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

    def test_find_link(self):
        requests.get = Mock()

        class Temp(object):
            text = """
              <html><a href= "http://docs.yahoo.co.jp/target"></a></html>
            """
        requests.get.return_value = Temp()
        printer = BrowserPrinter(self.config)

        self.assertEqual([Link('http://docs.yahoo.co.jp/target')], printer.find_link(Link('top')))

    def test_crawl(self):
        printer = BrowserPrinter(self.config)
        printer.find_link = MagicMock(return_value=[Link('http://docs.yahoo.co.jp/sample')])

        self.assertEqual([Link('http://docs.yahoo.co.jp/sample')], printer.crawl(Link('http://www.yahoo.co.jp')))

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
