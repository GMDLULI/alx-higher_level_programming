#!/usr/bin/python3
true = 1
false = 0
def islower(c):
    """function that checks for lowercase characters"""
    if ord(c) >= 97 and ord(c) <= 122:
        return true
    else:
        return false