#!/usr/bin/python3
"""
This function indents a text
"""

def text_indentation(text):
    """Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] ==' ':
        char +=1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ":.?":
            if text[char] in ":.?":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
