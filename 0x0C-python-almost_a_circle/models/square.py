#!/usr/bin/python3
"""
Docstripy for our rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
	"""Create Square class that inherits
    from Rectangle
	"""
	def __int__(self, size, x=0, y=0, id=None):
		"""Initialize a square"""
		super().__init__(size, size, x, y, id)

    @property
    def size(self):
		"""Get the size value"""
		return self.width

    @size.setter
    def size(self, value):
		self.width = size
		self.height = size

    def __str__(self):
		return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
