#!/usr/bin/python3
"""Module that defines the JSON representation"""
import json


def to_json_string(my_obj):
    """Function that returns JSON representaion of object"""
    return json.dumps(my_obj)
