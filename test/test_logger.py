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
        import six
        import datetime
        import time
        import glob
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

        if six.PY3:
            with open(filename, encoding="utf8") as file:
                data = file.read()
        elif six.PY2:
            with open(filename) as file:
                data = file.read().decode("UTF-8")
        else:
            return
        self.assertTrue("你好世界" in data)

        today = datetime.date.today()
        generate_filename = os.path.join(dirname, "*.{}.log".format(today))
        files = glob.glob(generate_filename)
        for name in files:
            os.remove(name)

        command = "sudo date -s 23:59:59"
        logger.debug(command)
        os.system(command)
        future = time.time() + 2
        while time.time() < future:
            logger.info("test for split file")
            time.sleep(0.1)

        files = glob.glob(generate_filename)
        self.assertTrue(file)
        command = "rm *.log"
        logger.debug(command)
        os.system(command)

        command = "sudo ntpdate cn.pool.ntp.org"
        logger.debug(command)
        os.system(command)


if __name__ == '__main__':
    unittest.main()
