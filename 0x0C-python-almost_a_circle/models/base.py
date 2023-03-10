#!/usr/bin/python3
"""Module that defines a class Base"""
import json


class Base:
    """class Base that manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """inistializes new Base.
        Args:
            id(int): the identity of the new base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns the JSON string representation
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Function that writes to json string respresentaion of
            object to file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            if not list_objs:
                list_objs = []

            for i in list_objs:
                list_dicts = [i.to_dictionary()]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of json string representaion
        """
        if json_string is None or not json_string:
            return []
        else:
            jstring = json.loads(json_string)
            return jstring

    @classmethod
    def create(cls, **dictionary):
        """Returnsa list of instances, by creating a new instance
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = "{cls.__name__}.json".format(cls.__name__)
        if not path.isfile(file_load):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            return[cls.create(**dic) for dic in cls.from__json_string(f.read())]
