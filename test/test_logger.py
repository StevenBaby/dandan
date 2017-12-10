# coding=utf8
from __future__ import print_function, unicode_literals, absolute_import
import unittest
import os
import sys

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if dirname not in sys.path:
    sys.path.insert(0, dirname)


class TestValue(unittest.TestCase):

    def test_logger(self):
        import dandan
        print(dandan)
        logger = dandan.logger.getLogger("test")

        logger.info("hello")
        

if __name__ == '__main__':
    unittest.main()
