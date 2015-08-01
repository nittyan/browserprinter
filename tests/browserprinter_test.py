# -*- coding:utf-8 -*-

import unittest
from browserprinter.printer import BrowserPrinter, Configure


class BrowserPrinterTestCase(unittest.TestCase):

    def test_configure(self):
        config = Configure({
            'top_page': 'http://www.yahoo.co.jp',
            'includes': ['http://docs.yahoo.co.jp'],
            'excludes': ['http://docs.yahoo.co.jp/info'],
            'dest_dir': 'screenshots',
            'driver': 'Firefox'
        })
        self.assertIsNotNone(config)

    def test_browserprinter(self):
        config = Configure({
            'top_page': 'http://www.yahoo.co.jp',
            'includes': ['http://docs.yahoo.co.jp'],
            'excludes': ['http://docs.yahoo.co.jp/info'],
            'dest_dir': 'screenshots',
            'driver': 'Firefox'
        })

        printer = BrowserPrinter(config)
        printer.execute()


if __name__ == '__main__':
    unittest.main()
