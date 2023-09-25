#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
	i = 0
	while i <= x:
	try:
		print(str(my_list[i]))
			i += 1
		return i
	except (RangeError):
		return i
