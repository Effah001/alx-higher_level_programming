#!/usr/bin/python3

def magic_calculation(a, b):
    calc = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            calc = calc + (a ** b) / i
        except Exception:
            calc = a + b
            break
    return calc
