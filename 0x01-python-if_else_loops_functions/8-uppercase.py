#!/usr/bin/python3

def uppercase(str):

    s = list(str)
    for c in range(len(s)):
        if ord(s[c]) >= 97 and ord(s[c]) <= 122:
            s[c] = chr(ord(s[c]) - 32)
        print("{}".format(("").join(s)))
