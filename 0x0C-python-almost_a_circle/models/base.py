#!/usr/bin/python3
"""Module that defines a class Base"""


class Base:
    """class Base that manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inistializes new Base.
        Args:
            id(int): the identity of the new base
        """

        if id is None:
            self.id = id
        else:
            Base.__nb_object +=1
            self.id = Base.__nb_objects
           
