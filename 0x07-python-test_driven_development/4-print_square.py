#!/usr/bin/python3
"""
A function that prints a square using # based on size
"""

def print_square(size):
    """
    print a square from the size given by the user
    
    Args:
        size: size of each row of the square
    """

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    size = int(size)
    for i in range(size):
        print("#" * size)

