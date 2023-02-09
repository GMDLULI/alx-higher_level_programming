#!/usr/bin/python3
"""This module defines a python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representaion of a simple data structure"""
    return obj.__dict__
