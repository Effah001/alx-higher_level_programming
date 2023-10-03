#/usr/bin/python3
"""A module to find the maximum integer in a list"""


def max_integer(list=[]):
    """A function that returns the maximum integer in a list
    if the list is empty, the function returns None"""

    if len(list) == 0:
        return None
    num = list[0]
    x = 1
    while x < len(list):
        if list[x] > num:
            num = list[x]
        x += 1
    return num
