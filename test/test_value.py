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
        filename = os.path.realpath(os.path.join(project, "dandan/__init__.py"))
        modulepath = os.path.realpath(dandan.__file__)
        self.assertEqual(os.path.splitext(modulepath)[0], os.path.splitext(filename)[0])

    def test_attrdict(self):
        import dandan

        data = dandan.value.AttrDict()
        data.key1 = 1
        assert(data.key1 == data["key1"])

        data = {
            "key1": 1,
            "key2": {
                "key21": 1,
            },
            "key3": [
                {
                    "key31": 1,
                    "key32": None,
                },
                234,
                "12345",
            ],
        }

        self.assertTrue(isinstance(data, dict))
        self.assertFalse(isinstance(data, dandan.value.AttrDict))
        self.assertTrue(isinstance(data["key3"], list))
        self.assertTrue(isinstance(data["key3"][0], dict))

        data = dandan.value.AttrDict(data)

        self.assertTrue(isinstance(data, dict))
        self.assertTrue(isinstance(data, dandan.value.AttrDict))
        self.assertTrue(isinstance(data["key3"], list))
        self.assertTrue(isinstance(data["key3"][0], dandan.value.AttrDict))

        self.assertEqual(data["key3"], data.key3)

    def test_length(self):
        import dandan

        self.assertEqual(dandan.value.length("test string"), 11)
        self.assertEqual(dandan.value.length("测试字符串"), 10)
        self.assertEqual(dandan.value.length("测试字符串 test string"), 22)

    def test_json(self):
        import dandan

        data = dandan.value.AttrDict()
        data.key1 = 1
        data.key2.key1 = 3

        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.json")
        if os.path.exists(filename):
            os.remove(filename)
        self.assertFalse(os.path.exists(filename))
        dandan.value.put_json(data, filename)
        with open(filename) as file:
            content = file.read()
        data = dandan.value.get_json(filename)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["key1"], 1)
        self.assertEqual(data["key2"]["key1"], 3)

        if os.path.exists(filename):
            os.remove(filename)
        self.assertFalse(os.path.exists(filename))
        dandan.value.put_json(data, filename, indent=4)
        data = dandan.value.get_json(filename)
        self.assertEqual(type(data), dict)
        self.assertEqual(data["key1"], 1)
        self.assertEqual(data["key2"]["key1"], 3)
        if os.path.exists(filename):
            os.remove(filename)

    def test_pickle(self):
        pass


    def test_md5(self):
        import dandan
        import six
        data = "hello, world!!! 你好，世界"
        self.assertEqual(dandan.value.md5(data), "dfef11310f36f88548d23a261c25269c")

        filename = os.path.join(dirname,"md5")

        if six.PY3:
            with open(filename, "w", encoding='utf8') as file:
                file.write(data)
        else:
            with open(filename, "w") as file:
                file.write(data.encode("utf8"))

        self.assertEqual(dandan.value.md5(filename=filename), "dfef11310f36f88548d23a261c25269c")
        os.remove(filename)

    def test_sha1(self):
        import dandan
        import six
        data = "hello, world!!! 你好，世界"
        self.assertEqual(dandan.value.sha1(data), "f452f30df683186f327ddf67a1c7c0fc59a64409")

        filename = os.path.join(dirname,"md5")

        if six.PY3:
            with open(filename, "w", encoding='utf8') as file:
                file.write(data)
        else:
            with open(filename, "w") as file:
                file.write(data.encode("utf8"))

        self.assertEqual(dandan.value.sha1(filename=filename), "f452f30df683186f327ddf67a1c7c0fc59a64409")

    def test_number(self):
        import dandan

        self.assertTrue(dandan.value.is_number(1234))
        self.assertTrue(dandan.value.is_number(1234.1234))
        self.assertTrue(dandan.value.is_number("1234"))
        self.assertFalse(dandan.value.is_number("hello world"))

        self.assertEqual(dandan.value.number(1234), 1234)
        self.assertEqual(dandan.value.number(1234.1234), 1234.1234)
        self.assertEqual(dandan.value.number("1234"), 1234)
        self.assertEqual(dandan.value.number("hello world"), None)


if __name__ == '__main__':
    unittest.main()
