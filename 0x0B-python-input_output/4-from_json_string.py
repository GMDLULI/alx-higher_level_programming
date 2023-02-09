#!/usr/bin/python3
"""Module that returns object represented by JSON"""


def from_json_string(my_str):
    """function that returns object represented by JSON"""
    obj = jason.loads(my_str)
    return obj
