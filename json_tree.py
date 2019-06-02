#!/usr/bin/env python3
"""
name: json_tree.py
description: reads strings from a file and displays json as nested trees
author: Eric Mattison
date: 2019-06-02
"""

class JsonTree:
    def __init__(self):
        self.filename = "inputTestCases.txt"
        self.strings = []

    def read_strings(self):
        """
        Read the input file and insert each line into an array.
        Strip out spaces, newlines, and tabs (I would ordinarily use a regular expression to remove whitespace,
        but if I'm reading the directions correctly, I'm not supposed to use outside packages).
        :return:
        """
        try:
            with open(self.filename) as f:
                for i, line in enumerate(f.readlines(), start=1):
                    clean_line = line.strip().replace(" ", "").replace("\t", "").replace("\n", "")
                    if self.check_json(i, clean_line):
                        self.strings.append(clean_line)
        except FileNotFoundError as e:
            print(f'Could not find file "{self.filename}".')
            raise
        except IOError as e:
            print(f'Could not read file "{self.filename}".  Please make sure the file is world-readable.')
            raise
        except:
            print("Unexpected Error:")
            raise

    def check_json(self, i, string):
        """
        A quick check to ensure that the json supplied is valid
        :return:
        """
        if not len(string):
            print(f"Empty string on line {i}.  Ignoring line.")
            return False
        if string.count("{") != string.count("}"):
            print(f"Mismatched braces on line {i}:")
            print(f"    {string}")
            print("    Ignoring line.")
            return False
        if string == "{}":
            print(f"Root object is empty on line {i}.  Ignoring line.")
            return False
        """
        Hmmm.  What if all of the nodes are empty, but there's still a structure?
        Stepping through the object structure here means a performance hit (I'm going to need to step through
        the JSON for each string already), so I'll hold off for now.  Maybe I'll do this check as I'm building the tree.
        """
        return True

if __name__ == "__main__":
    json_tree = JsonTree()
    json_tree.read_strings()
    for string in json_tree.strings:
        print(string)