#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

result = ()

for num in range(len(tuple_a)):
    result += (tuple_a[num] + tuple_b[num],)

print(result)
