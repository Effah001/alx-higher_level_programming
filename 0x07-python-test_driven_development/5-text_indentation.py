#!/usr/bin/python3
"""
This function indents a text
"""

def text_indentation(text):
    """Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    line = ""

    for char in text:

        if char in ".?:":
            line += char
            line = line.strip()
            line += "\n\n"
            result += line
            line = ""
        else:
            line += char
            if char.isspace():
                line = line.strip()
        result += line.strip()

    print(result, end="")
