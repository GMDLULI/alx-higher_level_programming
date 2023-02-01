#!/usr/bin/python3
"""
class that defines a rectangle
"""


class Rectangle:
  
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Function that defines a rectangle
        Args:
            self.__height = height
            self.__width = width
        Raise:
            TypeError: if height or width is not an integer
            ValueError: if height or width is < 0
         """
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """retrieves width attribute"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """retrieves height atrribute"""
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
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest rectangle base on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a square"""
        return Rectangle(size, size)
