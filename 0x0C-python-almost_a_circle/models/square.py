#!/usr/bin/python3
"""
Docstripy for our rectangle class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Creating Square class that inherits
    from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size value"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square"""
        attrs = ["id", "size", "x", "y"]
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictiory representation of a square"""
        square_dict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return square_dict

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
