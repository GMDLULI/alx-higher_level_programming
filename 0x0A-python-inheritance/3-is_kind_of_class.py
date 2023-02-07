#!/usr/bin/python3
"""Checks if instance is of class or class inherited from"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is instance of class or inherited class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
