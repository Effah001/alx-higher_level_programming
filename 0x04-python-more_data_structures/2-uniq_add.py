#!/usr/bin/python3 
def uniq_add(my_list=[]):
    result = 0
    uniq_set = set()
    
    for i in my_list:
        if i not in uniq_set:
            result += i
            uniq_set.add(i)
            
    return result
