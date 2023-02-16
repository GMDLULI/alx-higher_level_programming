#!/usr/python3
"""Module defines a Square class that inherits from
   Rectangle
"""


from models.rectangle import *


class Square(Rectangle):
    """Square class implementing Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """inistializes Square attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter function for size
           retuns: size
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter function for size
           Args:
               value (int): value to be set
        """
        if type(value) is not int:
            raise TypeError("width must be integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """function that assigns attributes to key/value arguments
           kwargs is skipped if args is not empty
           Args:
               *args - variable number of no-keyworded args
               **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """method returns a string"""
        return "[{}] ({}) {}/{} - {}". format(type(self).__name__,
                                              self.id,
                                              self.x, self.y,
                                              self.width)

    def to_dictionary(self):
        """Returns dictionary representaion of a Square"""

        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'y': getattr(self, "y"),
                'x': getattr(self, "x")}
