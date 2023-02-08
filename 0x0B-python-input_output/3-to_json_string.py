#!/usr/bin/python3
import json
"""Module that defines the JSON representation"""


def to_json_string(my_obj):
    """Function that returns JSON representaion of object"""
    print(json.dumps(my_obj), end="")
