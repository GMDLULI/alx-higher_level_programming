#!/usr/python3
"""
Module that defines a class Rectangle
"""
from models.base import Base


class Rectangle(base):
    """class REctangle implements Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initilize Rectangle class
        Args:
            width: width
            height: height
            x: x variable
            y: y varible 
        """
        super().__init__(id) 
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @getter
    def width(self):
        """getter function for with
           returns: width
        """
        return self.width

    @width.setter
    def width(self, value):
        """setter function for width
         Args:
            value (int): value to be set
        """
        if type(width) is not int:
            raise TypeError("width must be integer")

        if width <= 0:
            rasie ValueError("width must be > 0")

        self.__width = value
    
    @getter
    def height(self):
        """getter function for height
           returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for height
         Args:
            value (int): value to be set
         """
        if type(height) is not int:
            raise TypeError("height must be integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = value


    @getter
    def x(self):
        """getter function for x
           returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter function for x
         Args:
            value (int): value to be set
         """
        if type(x) is not int:
            raise TypeError("x must be integer")

        if x <= 0:
            rasie ValueError("x must be > 0")
        self.__width = value


    @getter
    def y(self):
        """getter function for y
           returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter function for x
         Args:
            value (int): value to be set
         """
        if type(y) is not int:
            raise TypeError("y must be integer")

        if y <= 0:
            rasie ValueError("y must be > 0")
        self.__y = value
