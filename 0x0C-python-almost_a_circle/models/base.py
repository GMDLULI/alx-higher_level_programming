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
        if list_dictionaries is None or list_dictionaries = "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Function that writes to json string respresentaion of
            object to file
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) <= 0:
                f.write("[]")

            for i in list_objs:
                list_dicts = i.to_dictionary()
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of json string representaion
        """
        if json_string is None:
            return
        else:
            jstring = json.loads(json_string)
            return jstring

    @classmethod
    def create(cls, **dictionary):
        """Returnsa list of instances, by creating a new instance
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r", encoding="utf-8") as jsonfile:
                string = jsonfile.read()
                save = cls.from_json_string(string)
                return [cls.create(**d) for d in save]

        except (IOError):
            return []
