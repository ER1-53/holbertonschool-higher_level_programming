#!/usr/bin/python3
"""Square of the project"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Display informations"""
        class_name = self.__class__.__name__
        id = self.id
        w = self.width
        return f"[{class_name}] ({id}) {self.x}/{self.y} - {w}"
    
    def update(self, *args, **kwargs):
        """update from parents Rectangle"""
        super().update(*args, **kwargs)

    def to_dictionary(self):
        """__dict__"""
        return {
                'id': self.id,
                'x': self.x,
                'size': self.height,
                'y': self.y
            }
