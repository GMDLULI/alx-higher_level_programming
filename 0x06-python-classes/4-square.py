#!/usr/bin/python3
"""class 'Square' that defines a square by:
    (based on 3-square.py)
"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be integer')

        if size < 0:
            raise ValueError('size must be >=0')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2
