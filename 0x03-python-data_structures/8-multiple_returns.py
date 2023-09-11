#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == []:
        sentence[0] = None
        first = sentence[0]
        length = len(sentence)
    else:
        length = len(sentence)
        first = sentence[0]
    print("{:d} - First character: {}".format(length, first))
