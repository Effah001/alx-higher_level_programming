#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            a = 0
            print("division by 0")
        except TypeError:
            a = 0
            print("wrong type")
        except IndexError:
            a = 0
            print("out of range")
        finally:
            result.append(a)
    return result
