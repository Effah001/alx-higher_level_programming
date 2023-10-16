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
        if args and len(args) > 0:
         for i, arg in enumerate(args):
             if i < len(attrs):
                 setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
