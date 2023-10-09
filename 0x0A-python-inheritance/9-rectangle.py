#!/usr/bin/python3
"""
A Rectangle function that inherits from
BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_Geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass of BaseGeometry"""
    def __init__(self, width, height):

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        def area(self):
            return self.__width * self.__height

        def __str__(self):
            return f"[Rectangle] {self.__width}/{self.__height}"
