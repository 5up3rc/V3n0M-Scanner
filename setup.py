#!/usr/bin/env python
from distutils.core import setup
import setuptools

setup(name='V3n0M',
      version='411',
      description="Popular SQLi and Pentesting scanner in Python3",
      author='NovaCygni, Architect',
      author_email='novacygni@hotmail.co.uk, t3h4rch1t3ct@riseup.net,',
      url='https://github.com/v3n0m-Scanner/V3n0M-Scanner',
      package_dir={'v3n0m': 'src'},
      packages=['v3n0m'], install_requires=['aiohttp', 'httplib2', 'socksipy-branch', 'requests', 'url', 'bs4',
                                            'pip', 'dnspython']
      )
