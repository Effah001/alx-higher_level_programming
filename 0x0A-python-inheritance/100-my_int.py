#!/usr/bin/python3
"""
 A class MyInt that inherits from int
"""


class MyInt(int):
    """MyInt has == and != operators inverted"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
