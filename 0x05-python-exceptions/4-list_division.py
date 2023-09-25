#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        a = 0
        try:
            a = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
        except ZerodivisionError:
            print("dividing by 0")
        except IndexError:
            print("Out of range")
        else:
            pass
        finally:
            result.append(x)
        return result
