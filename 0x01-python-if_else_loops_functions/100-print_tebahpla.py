#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    if x % 2 == 0:
        c = 0
    else:
        c = 32
    print('{}'.format(chr(x - c)), end="")
