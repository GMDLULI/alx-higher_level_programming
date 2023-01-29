#!/usr/bin/python3
"""
This module is composed of a function that prints a square with the character #
"""


def print_square(size):
    """ Function that prints a sqaure with character #
    Args:
        size: size of square
    Returs:
        No return
    Raises:
        TypeError: is size is not an integer number
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print("#" * size)
