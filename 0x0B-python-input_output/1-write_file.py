#!/usr/bin/python3
"""Module that defines a text - writing file function"""


def write_file(filename="", text=""):
    """Function wites a string to a text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
