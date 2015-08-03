# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import selenium.webdriver as webdriver
from urllib.parse import urlparse
import os


class BrowserPrinter(object):

    def __init__(self, conf):
        self.conf = conf
        self._make_dest_dir()

    def _make_dest_dir(self):
        if not os.path.exists(self.conf.dest_dir):
            os.mkdir(self.conf.dest_dir)

    def execute(self):
        urls = self.crawl(self.conf.top, [self.conf.top])
        self.get_screenshots(urls)

    def crawl(self, top, links=[]):
        hrefs = self.find_link(top)
        for link in hrefs:
            if self.do_crawl(link, links):
                links.append(link)
                self.crawl(link, links)
        return links

    def do_crawl(self, link, links):
        return self.conf.contains_include(link) and not self.conf.contains_exclude(link) and not self.did_crawl(link, links)

    def did_crawl(self, link, links):
        return link in links

    def find_link(self, url):
        html = self.get_html(url)
        print('parsing {0}'.format(url))
        soup = BeautifulSoup(html, 'html.parser')
        return list(map(lambda o: o.get('href'), soup.find_all('a')))

    def get_html(self, url):
        return requests.get(url).text

    def get_screenshots(self, urls):
        browser = self.get_driver()
        counter = 1
        for url in urls:
            browser.get(url)
            browser.save_screenshot(self._create_file_path(str(counter)))
            counter += 1
        browser.quit()

    def _create_file_path(self, file_name):
        return self.conf.dest_dir + os.sep + file_name + '.png'

    def get_driver(self):
        if 'Firefox' is self.conf.driver_name:
            return webdriver.Firefox()
        elif 'Chrome' is self.conf.driver_name:
            return webdriver.Chrome()
        elif 'Ie' is self.conf.driver_name:
            return webdriver.Ie()
        elif 'Opera' is self.conf.driver_name:
            return webdriver.Opera()
        else:
            raise "Invalid driver"


class Link(object):

    def __init__(self, url):
        self.url = url

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, Link):
            return False

        return self.url == other.url

    def is_valid(self):
        if self.url is None or '' is self.url:
            return False

        parsed = urlparse(self.url)
        if 'http' != parsed.scheme and 'https' != parsed.scheme:
            return False
        if '' == parsed.netloc:
            return False
        if '' != parsed.fragment:
            return False

        return True

    def do_crawl(self, includes, excludes):
        if self._is_includes(includes) and not self._is_excludes(excludes):
            return True
        return False

    def _is_includes(self, includes):
        parsed = urlparse(self.url)
        return parsed.scheme + '://' + parsed.netloc in includes

    def _is_excludes(self, excludes):
        for ex in excludes:
            if self.url.startswith(ex):
                return True
        return False


class Configure(object):

    def __init__(self, conf):
        self.conf = conf
        self.driver_name = self.conf['driver']
        self.top = self.conf['top_page']
        self.dest_dir = self.conf['dest_dir']
        self.includes = self.conf['includes']
        self.excludes = self.conf['excludes']

    def contains_include(self, url):
        if url is None:
            return False
        parsed = urlparse(url)
        return parsed.scheme + "://" + parsed.netloc in self.includes

    def contains_exclude(self, url):
        if url is None:
            return False
        for ex in self.excludes:
            if url.startswith(ex):
                return True
        return False

