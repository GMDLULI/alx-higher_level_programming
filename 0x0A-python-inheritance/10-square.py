#!/usr/bin/python3
"""Module that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square that inherits Rectangle"""

    def __init__(self, size):
        """Initialize a new square
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """Returns the dimension of the square"""
        result = "[" + self.__class__.__name__ + "] "
        result += str(self.__size) + "/" + str(self.__size)
        return result
