#!/usr/bin/python3
"""Module that returns object represented by JSON"""


import json


def from_json_string(my_str):
    """function that returns object represented by JSON"""
    return json.loads(my_str)
