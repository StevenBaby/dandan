from __future__ import print_function, unicode_literals, absolute_import
import unittest
import os

filename = os.path.abspath(__file__)
dirname = os.path.dirname(filename)


class TestValue(unittest.TestCase):

    def test_attrdict(self):
        import dandan
        print(dandan)

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
