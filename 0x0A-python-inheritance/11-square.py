#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
 a class Square inheritance from BaseGeometry
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def  __str__(self):
        return f"[square] {self.__size}/{self.__size}"
