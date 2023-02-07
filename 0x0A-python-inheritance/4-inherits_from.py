#!/usr/bin/python3
"""Checks if instance is object of class"""


def inherits_from(obj, a_class):
    """Return true if object is an instance of a class that
       inherited (directly or indirectly)"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
