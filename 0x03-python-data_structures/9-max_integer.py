#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        max = my_list[0]
        for num in range(1, len(my_list)):
            if my_list[num] > max:
                max = my_list[num]
        return (max)
