#!/usr/bin/python3
"""
A class that defines a rectangle
"""

class Rectangle:
    """A class that defines a rectangle"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """instantiating of the class"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__ (self):
        """output of the rectangle"""
        if self.__width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """String representation of the Rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"
