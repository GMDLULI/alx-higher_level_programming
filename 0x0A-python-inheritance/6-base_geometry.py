#!/usr/bin/python3
"""Module condist of a class that raises an exception"""


class BaseGeometry:
    def area(self):
        """ Function that raises an exception with message"""

        raises Exception("area() is not implemented")
