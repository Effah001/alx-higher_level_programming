#!/usr/bin/python3
"""
The docscript for our rectangle class
"""

class Base:
    def __init__(self, id=None):
        self.id = id

class Rectangle(Base):
    """ Create Rectangle class that inherits
    from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if width < 0 or height < 0:
            raise ValueError("Width and height nust be positive integers")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height= height

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y
