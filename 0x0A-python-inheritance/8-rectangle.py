#!/usr/bin/python3
"""Inherits from BaseGEometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from the BaseGeometry"""

    def __init__(self, width, height):
        """initialize new rectangle"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
