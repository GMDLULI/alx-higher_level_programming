#!/usr/bin/python
"""
class that defines a rectangle
"""


class Rectangle:
    """ Function that defines a rectangle
    Args:
        self.__height = height
        self.__width = width
    Raise:
        TypeError: if height or width is not an integer
        ValueError: if height or width is < 0
    Return:
        print rectangle with character "#"
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns th perimeter of the rectangle"""
        return ((self.__height * 2) + (self.__width * 2))
        if self.__height == 0 or self.__width == 0:
            return 0

    def __str__(self) -> str:
        """Presents a diagram of the rectangle defined fron object"""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rectangle = ""
        for i in range(self.__width):
            for d in range(self.__height):
                rectangle += "#"

            if i < self.__height - 1:
                rectangle += '\n'
        return (rectangle)

    def __repr__(self):
        """Presents the representation of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints message when instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
