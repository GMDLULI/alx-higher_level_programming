#!/usr/bin/python3
"""class `Square` defines a square by:
    (based on 0-square.py)

"""


class Square:
    """defines a 'Square'
    * Private insatnce attribute: 'size'
    * Instantiation with 'size' (no type/value verification)
    """
    def __init__(self, size):
        self.__size = size
