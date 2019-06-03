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

    def test_build_object(self):
        result = self.jtree.build_object("{Anakin{Luke,Leia},Han{Kaylo}}")
        expected = [{'word': 'Anakin', 'depth': 0},
                    {'word': 'Luke', 'depth': 1},
                    {'word': 'Leia', 'depth': 1},
                    {'word': 'Han', 'depth': 0},
                    {'word': 'Kaylo', 'depth': 1}]
        self.assertEqual(result, expected)
        self.assertRaises(ValueError, self.jtree.build_object, "{{foo}{bar, baz}}")  #No comma
        self.assertRaises(ValueError, self.jtree.build_object, "{foo{}bar{}}")  #No comma

    def test_display_tree(self):
        result = self.jtree.display_tree([{'word': 'Anakin', 'depth': 0},
                                          {'word': 'Luke', 'depth': 1},
                                          {'word': 'Leia', 'depth': 1},
                                          {'word': 'Han', 'depth': 0},
                                          {'word': 'Kaylo', 'depth': 1}], alpha=None)
        expected = ['Anakin', '-Luke', '-Leia', 'Han', '-Kaylo']
        self.assertEqual(result, expected)
        result = self.jtree.display_tree([{'word': 'Anakin', 'depth': 0},
                                          {'word': 'Luke', 'depth': 1},
                                          {'word': 'Leia', 'depth': 1},
                                          {'word': 'Han', 'depth': 0},
                                          {'word': 'Kaylo', 'depth': 1}], alpha=True)
        expected = ['Anakin', 'Han', '-Kaylo', '-Leia', '-Luke']
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()