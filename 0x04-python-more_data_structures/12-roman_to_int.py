#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    x = 0
    for a in range(len(roman_string) - 1):
        if digits[roman_string[a]] < digits[roman_string[a+1]]:
            x -= digits[roman_string[a]]
        else:
            x += digits[roman_string[a]]
    x += digits[roman_string[-1]]
    return x
