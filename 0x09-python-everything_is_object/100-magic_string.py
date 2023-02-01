#!/usr/bin/python3
def magic_string():
    magic_string.iterator = getattr(magic_string, 'iterator', 0) + 1
    return ", ".join("BestSchool" for _ in range(magic_string.iterator))
