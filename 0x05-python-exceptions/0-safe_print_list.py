#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	try:
		i = 0
		while i <= x:
			print(str(my_list[i]))
			i += 1
		return i
	except (RangeError):
		return i
