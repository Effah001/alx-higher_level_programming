#!/usr/bin/python3

def uniq_add(my_list=[]):
    num = 0
    uniq = set(my_list)
    for item in uniq:
        num += item
    return num
