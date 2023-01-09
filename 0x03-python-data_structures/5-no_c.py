#!/usr/python3

def no_c(my_string):
    new_str = my_string.translate({ord('c'): None})
    new_str = new_str.translate({ord('C'): None})
    return new_str
