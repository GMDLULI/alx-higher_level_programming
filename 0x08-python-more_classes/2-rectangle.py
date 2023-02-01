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
             area of rectangle
                  parimeter of rectangle
         """
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
        """retrives width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """retrieves width attribute"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """retrieves height atrribute"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of rectangle"""
        return ((self.__height * 2) + (self.__width * 2))
        if height == 0 or width == 0:
            return 0
