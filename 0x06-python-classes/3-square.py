#!/usr/bin/python3
"""class `Square` that defines a square by:
    (based on 2-square.py)

	
	"""
class Square:
    """defines a square
    * Private instace attribute: 'size'
    * Instantiation with optional 'size': def __init__(self, size=00):
        * 'size' must be an integer, othwerwise raise TypeError
        * if 'size' is less than 0, raise a ValueError
     * Public instance method: def area(self):
     """
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """returns: the current square area"""
        return self.__size ** 2
