#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry"""
    def area(self):
        """Method that raises an exception with message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be greater than 0")
