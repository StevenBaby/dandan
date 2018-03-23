#! coding=utf-8
from __future__ import print_function, unicode_literals
import sys
import os
import glob
import unittest
import six

if six.PY2:
    reload(sys)
    sys.setdefaultencoding("utf8")

dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if dirname not in sys.path:
    sys.path.insert(0, dirname)


def test_all():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(test_dir, "test_*.py")
    files = glob.glob(filename)

    module_names = map(lambda f: os.path.splitext(os.path.basename(f))[0], files)
    modules = map(__import__, module_names)

    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))


if __name__ == '__main__':
    unittest.main(defaultTest="test_all")
