#!/usr/bin/env python

try:#handy to build eggs if possible so people can easy_install
    from setuptools import setup
except:#distutils fallback
    from distutils.core import setup

import ioLabs
setup(name='ioLab',
      version=ioLabs.__version__,
      description='ioLab response box library',
      author='John Montgomery',
      url='http://www.ioLab.co.uk/',
      py_modules=['ioLabs', 'psyscopex'],
      packages=['hid'],
     )