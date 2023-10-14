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
        """Get the width value"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be greater than zero")
        self.__width = width

    @property 
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the width value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be greater than zero")
        self.__height= height

    @property
    def x(self):
        """Get the x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be greater than zero")
        self.__x = x

    @property
    def y(self):
        """Get the y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <0:
            raise ValueError("y must be greater than zero")
        self.__y = y
