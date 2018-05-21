# coding=utf8
from __future__ import print_function, unicode_literals, absolute_import
import unittest
import os
import sys

dirname = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(dirname)
if project not in sys.path:
    sys.path.insert(0, project)


class TestCase(unittest.TestCase):

    def test_import(self):
        import dandan

        @dandan.utils.interrupt
        def test_function():
            return True

        self.assertFalse(test_function())


if __name__ == '__main__':
    unittest.main()
