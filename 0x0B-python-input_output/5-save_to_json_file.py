#!/usr/bin/python3
"""Module that writed object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an oject to text file usinf JSON"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
