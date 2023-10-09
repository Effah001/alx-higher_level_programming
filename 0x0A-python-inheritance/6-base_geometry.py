#!/usr/bin/python3
"""
A class based on BaseGeometry
"""


class BaseGeometry:
    """
    Public instance method: def area(self): 
    that raises an Exception with the message area() is not implemented
    """
    def area(self):
        """gets the area"""
        raise Exception("area() is not implemented")
