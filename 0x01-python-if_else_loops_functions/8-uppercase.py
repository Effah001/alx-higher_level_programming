#!/usr/bin/python3
def uppercase(str):
    Upper = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        Upper += c
    print("{}\n".format(Upper), end="")
