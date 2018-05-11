# coding=utf8
from __future__ import print_function, unicode_literals, absolute_import
import unittest
import os
import sys
import warnings

dirname = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(dirname)
if project not in sys.path:
    sys.path.insert(0, project)


class TestCase(unittest.TestCase):

    def test_soup(self):
        warnings.filterwarnings("ignore")
        import dandan

        soup = dandan.query.soup("http://www.baidu.com")
        title = soup.select_one("title").get_text()
        self.assertEqual(title, "百度一下，你就知道")

    def test_local_ip(self):
        import dandan
        ip = dandan.query.local_ip()
        self.assertTrue(ip)
        self.assertEqual(len(ip.split(".")), 4)

    def test_html(self):
        import dandan
        html = dandan.query.html("http://www.baidu.com")
        self.assertTrue(html)
        self.assertTrue("百度一下，你就知道" in html)


if __name__ == '__main__':
    unittest.main()
