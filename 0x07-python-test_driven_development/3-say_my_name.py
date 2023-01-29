#!usr/bin/python3

"""
This module is composed by a function to print a message"
"""


def say_my_name(first_name, last_name=""):
    """function that rints my name is <first_name> <last_name>
    Args:
        first_name = first name
        last_ name = last name
    Raises:
        TypeError: if first_name or last_name is not a string
    Returns:
        No return
    """

    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")

    print(f"My name is {first_name} {last_name}")
