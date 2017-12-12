# coding=utf8
from __future__ import print_function, unicode_literals, absolute_import
import unittest
import os
import sys

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if dirname not in sys.path:
    sys.path.insert(0, dirname)


class TestValue(unittest.TestCase):

    def test_execute(self):
        import dandan
        print(dandan)

        result, code = dandan.system.execute("dir")
        print(result)
        print(code)

        dandan.system.execute("dir", callback=lambda line: print(line))


if __name__ == '__main__':
    unittest.main()
