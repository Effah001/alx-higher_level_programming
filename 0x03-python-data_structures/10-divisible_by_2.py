#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for num in my_list:
        if num % 2 == 0:
            print("{:d} is divisible by 2".format(num))
        else:
            print("{:d} is not divisible by 2".format(num))
