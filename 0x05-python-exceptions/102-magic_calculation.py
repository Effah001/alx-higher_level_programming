#!/usr/bin/python3

def magic_calculation(a, b):
    calc = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("very far")
            calc = calc + (a ** b) / x
        except Exception:
            calc = a + b
            break
    return calc
