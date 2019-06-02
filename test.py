#!/usr/bin/env python3
"""
name: test.py
description: tests for JsonTree Class
author: Eric Mattison
date: 2019-06-02
"""
import unittest
from json_tree import JsonTree

class TestJsonTree(unittest.TestCase):
    def setUp(self):
        self.jtree = JsonTree()

    def test_init(self):
        self.assertGreater(len(self.jtree.filename), 0)

    def test_read_strings(self):
        self.jtree.read_strings()
        self.assertGreater(len(self.jtree.strings), 0)

    def test_check_json(self):
        result = self.jtree.check_json(3, "")
        self.assertEqual(result, False)
        result = self.jtree.check_json(1, "{{{}}")
        self.assertEqual(result, False)
        result = self.jtree.check_json(1, "{}")
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()