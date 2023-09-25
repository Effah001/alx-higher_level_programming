#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

	i = 0

	for a in range(x):
		try:
			print(f"{my_list[a]}", end="")
		except IndexError:
			pass
		else:
			i += 1
	print()
	return i
