#!/usr/bin/python3
"""Module that writed object to text file"""


def save_to_json_file(my_obj, filename):
    """writes an oject to text file usinf JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dumps(my_obj, f)
