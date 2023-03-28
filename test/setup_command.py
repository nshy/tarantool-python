#!/usr/bin/env python
"""
This module describes class implementing `python setup.py test`.
"""

import os
import sys
import unittest
from distutils.errors import DistutilsError
from glob import glob

import setuptools

class Test(setuptools.Command):
    """
    Class implementing `python setup.py test`.
    """

    user_options = []
    description = 'Run tests'

    def initialize_options(self):
        """
        Do nothing. setuptools requires to override this abstract
        method.
        """
        pass

    def finalize_options(self):
        """
        Do nothing. setuptools requires to override this abstract
        method.
        """
        pass

    def run(self):
        """
        Find all tests in test/tarantool/ and run them
        """

        tests = unittest.defaultTestLoader.discover('test', pattern='suites')
        test_runner = unittest.TextTestRunner(verbosity=2)
        result = test_runner.run(tests)
        if not result.wasSuccessful():
            raise DistutilsError('There are failed tests')
