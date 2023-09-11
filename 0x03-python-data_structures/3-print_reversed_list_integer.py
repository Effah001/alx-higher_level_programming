#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reversed = list(reversed(my_list))
    for element in reversed:
        print("{:d}".format(element))
