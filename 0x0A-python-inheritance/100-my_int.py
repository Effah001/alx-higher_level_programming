#!/usr/bin/python3
"""
 A class MyInt that inherits from int
"""


class MyInt(int):
    def __eq__(self, value):
        return int.__eq__(self, value)

    def __ne__(self, value):
        return int.__ne__(self, value)



