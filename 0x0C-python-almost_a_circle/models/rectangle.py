#!/usr/python3
"""
Module that defines a class Rectangle
"""
from models.base import Base


class Rectangle(Base):
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

    @property
    def width(self):
        """getter function for with
           returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width
         Args:
            value (int): value to be set
        """
        if type(value) is not int:
            raise TypeError("width must be integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
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
        if type(value) is not int:
            raise TypeError("height must be integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
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
        if type(value) is not int:
            raise TypeError("x must be integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
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
        if type(value) is not int:
            raise TypeError("y must be integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that returns the area of Rectangle"""
        return self.__height * self.__width

    def display(self):
        """function that displays '#' character"""
        rect = ""
        symbol = "#"
#        for i in range(self.height - 1):
#           rect += symbol * self.__width + "\n"
#       rect += symbol * self.__width

#        print("{}".format(rect))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rect += (" " * self.x) + (symbol * self.width) + "\n"
        print(rect, end="")

    def __str__(self):
        """function that returns string"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
       """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """function that returns the dictionary
           representaion of a rectangle
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
