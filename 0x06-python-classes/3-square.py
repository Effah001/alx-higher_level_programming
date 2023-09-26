#!/usr/bin/python3

"""Create a Square class"""


class Square:
    """Initializes a sqaure"""

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
