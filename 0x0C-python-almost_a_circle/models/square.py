#!/usr/python3 
"""Module defines a Square class that inherits from
   Rectangle
"""


from models.Rectangle import Rectangle 

class Square(Rectangle):
    """Square class implementing Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """inistializes Square attributes"""
        super().__init__(id, x, y, width=size, height=size)
        self.size = size

        @property
        def size(self):
            """getter function for size
               retuns: size
            """
            return self.__size

       @size.setter
       def size(self, value):
           """setter function for size
              Args:
                  value (int): value to be set
           """
           if type(value) is not int:
               raise TypeError("size must be integer")
           if value <= 0:
               raise ValueError("size must be > 0")

    def __str__(self):
        """method returns a string"""
        return "[{}] ({}) {}/{} - {}". format(type(self.__name__, self.id,
                                                   self.__x, self.__y, 
                                                   self.__size))
