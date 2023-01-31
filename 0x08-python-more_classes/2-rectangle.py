#!/usr/bin/python
"""
This module compose of a function that defines a rectangle
"""


class Rectangle:
    """ Function that defines a rectangle
    Args:
        self.__height = height
        self.__width = width
    Raise:
        TypeError: if height or width is not an integer
        ValueError: if height or width is < 0
    Return:
        no return
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property        
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return ((self.__height *2) + (self.__width *2))
        if height == 0 or width == 0:
            return 0
