# -*- coding:utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='BrowserPrinter',
    version='0.1.0',
    description='browser screenshot',
    url='https://github.com/nittyan/browserprinter',
    author='nittyan',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alphat',
        'Topic :: Software Development :: Web utilityf',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4'
    ],

    keywords='screenshot browser crawl',
    packages=find_packages(exclude=['docs', 'tests']),
    extras_require={
        'dev': ['beautifulsoup4', 'selenium', 'requests']
    }
)
