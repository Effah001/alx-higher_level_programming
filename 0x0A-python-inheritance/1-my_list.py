#!/usr/bin/python3
"""
Documentation of inherit from class list
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """
    def print_sorted(self):
        """prints sorted elements
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
