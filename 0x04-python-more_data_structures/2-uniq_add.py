#!/usr/bin/bash/python3 
def uniq_add(my_list=[]):
    result = 0
    uniq_set = set()
    
    for i in my_list:
        if i not in unique_set:
            result += i
            uniq_set.add(i)
            
            print("Result: {:d}".format(result))