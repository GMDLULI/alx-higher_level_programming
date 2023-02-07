#!/usr/bin/python3
"""Module that inherits from Rectangle"""
Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """Class square that inherits Rectangle"""
    def __init__(self,size):
        """Initialize a new square
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        pass
