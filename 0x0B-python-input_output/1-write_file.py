#!/usr/bin/python3
"""Module that defines a text - writing file"""


def write_file(filename="", text=""):
    """Function wites a string to text file and return number of characters"""
    with open(filename ,"w", encoding="utf-8") as f
    print(f.write(text), end="")
