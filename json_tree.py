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

    def build_object(self, string):
        """
        Build an object which contains the words and their depth levels
        Loop through the string by character.  If { is found, increase depth.  If } is found, decrease depth.
        Use , { } as word separators.
        :param string:
        :return:
        """
        word_obj = []    #Ordinarily would use an OrderedDict here, but again, no outside packages.
        current_word = ""
        current_depth = -1
        for i, char in enumerate(string):
            if char not in ["{", "}", ","]:
                current_word += char
            else:
                if current_word:     #Don't add in case the previous character was "{", "}" or ","
                    word_obj.append({'word': current_word, 'depth': current_depth})
                    current_word = ""
                if char == "{":
                    if i > 0 and string[i - 1] in ["{", "}", ","]:
                        """
                        Special case: "}{" means badly formed JSON.  Raise a Value Error.
                        """
                        raise ValueError("Invalid JSON.  JSON objects must be preceded by a word.")
                    current_depth += 1
                if char == "}":
                    if i < len(string) - 1 and string[i + 1] not in ["}", ","]:
                        """
                        Special case: A } must be followed by either a { or a ,
                        """
                        raise ValueError("Invalid JSON.  A } must be followed by either another } or a , .")
                    current_depth -= 1
        return word_obj

    def display_tree(self, word_list, alpha=None):
        """
        Loop through the word_obj and display each line preceded by the number of dashes
        :param self:
        :param word_list:
        :param alpha: boolean to sort by alphabetical order
        :return:
        """
        lines = []
        if alpha:
            word_list = sorted(word_list, key=lambda k: k['word'])
        for word_obj in word_list:
            line = "{0}{1}".format("-" * word_obj.get('depth'), word_obj.get('word'))
            lines.append(line)    #mainly here for testing
            print(line)
        return lines


if __name__ == "__main__":
    """
    Ask user for input to avoid using sys.argv for command line args
    """
    alpha = None
    alpha_answer = input('Do you want to display results by alphabetical order? [Y/n]: ')
    if "y" in alpha_answer.lower()[:1]:
        alpha = True
    json_tree = JsonTree()
    json_tree.read_strings()
    for string in json_tree.strings:
        word_list = json_tree.build_object(string)
        json_tree.display_tree(word_list, alpha=alpha)
    #word_list = json_tree.build_object(json_tree.strings[3])
    #json_tree.display_tree(word_list)
    #for string in json_tree.strings:
    #    build_object(string)
