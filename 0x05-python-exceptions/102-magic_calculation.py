#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for x in range(1, 3):
        try:
            if i > a:
                raise Exception("very far")
            result = result + (a ** b) / i
        except Exception:
            result = a + b
            break
    return result
