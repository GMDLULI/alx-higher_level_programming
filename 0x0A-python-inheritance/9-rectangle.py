#!/usr/bin/python3
"""Module that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialze new Rectangle
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height - height
        self.integer_validator("height", height)

    def area(self):
        """Return Rectangle"""
        return self.__height * self.__width
