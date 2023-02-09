#!/usr/bin/python3
"""Module that defines a text file-appending function"""


def append_write(filename="", text=""):
    """FUnction that appends a string at the end of text file"""
    with open(filename, "a", encoding="utf-8") as f:
        print(f.write(text), end="")
