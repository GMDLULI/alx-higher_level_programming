#!/usr/bin/python3
"""This module checks if instance is of class"""


def is_same_class(obj, a_class):
    """Retur true if object is instance of class"""
    if type(obj) is a_class:
        return True
    else:
        return False
