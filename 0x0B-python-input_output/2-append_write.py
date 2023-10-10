#!/usr/bin/python3
"""documentation for appendind write function"""


def append_write(filename="", text=""):
    """open a file, create if it doesn't exist"""
    with open(filename, 'a') as f:
        return f.write(text)
