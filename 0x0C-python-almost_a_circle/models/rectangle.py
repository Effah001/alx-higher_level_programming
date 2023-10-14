#!/usr/bin/python3
"""
The docscript for our rectangle class
"""

from models.base import Base

class Rectangle(Base):
    """ Create Rectangle class that inherits
    from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None)
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise TypeError("width must be greater than zero")
        self.__width = width

    @property 
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise TypeError("height must be greater than zero")
        self.__height= height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be greater than zero")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <0:
            raise TypeError("y must be greater than zero")
        self.__y = y
