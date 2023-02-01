#!/usr/bin/python3
"""
Class that defines a rectangle
"""


class Rectangle:
    """this represents a rectangle"""

    def __init__(self, width=0, height=0):
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
        self.__height = height
        self.__width = width

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
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrives height attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError('height must be integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
