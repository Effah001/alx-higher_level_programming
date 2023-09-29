#!/usr/bin/python3

def add_integer(a, b=98):
	"""
	Adds two intgers.

	Args:
		a : first intger
		b : Second intger. Default is 98

	Returns:
		int: Sum of a and b
	"""	

	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("a must be an integer or b must be an integer")

	a = int(a)
	b = int(b)

	return a + b
