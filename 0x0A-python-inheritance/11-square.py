#!/usr/bin/python3
"""Import the Rectangle class, for operations"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class defines the dimension for a square object using
    methods inherited from Rectangle
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__("size", size)

    def area(self):
        """returns the area of a square"""
        return (self.__size ** 2)

    def __str__(self):
        """Returns the dimension of the square"""
        result = "[" + self.__class__.__name__ + "] "
        result += str(self.__size) + "/" + str(self.__size)
        return result
