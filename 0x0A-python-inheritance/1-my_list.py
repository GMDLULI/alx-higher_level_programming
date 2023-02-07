#!/usr/bin/python3
"""This module  inherits from the list"""


class MyList(list):
    """A class the inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
