# coding=utf-8
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
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dandan.log")
        if os.path.exists(filename):
            os.remove(filename)
        self.assertFalse(os.path.exists(filename))
        logger = dandan.logger.getLogger(filename=filename)
        logger.info("hello")
        self.assertTrue(os.path.exists(filename))
        logger.info("你好世界")
        self.assertTrue(os.path.exists(filename))

        with open(filename, encoding="utf8") as file:
            data = file.read()
        self.assertTrue("你好世界" in data)


if __name__ == '__main__':
    unittest.main()
