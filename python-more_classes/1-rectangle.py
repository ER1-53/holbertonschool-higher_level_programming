#!/usr/bin/python3
"""
It's class Rectangle for creat a rectangle.
"""


class Rectangle:

    """
Initializes a new Rectangle.
Args:
- width (int): The width of the rectangle (default is 0).
- height (int): The height of the rectangle (default is 0).
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        if not isinstance(self.width, int):
            raise TypeError("width must be an integer")
        if self.width < 0:
            raise ValueError("width must be >= 0")

    def height(self):
        if not isinstance(self.height, int):
            raise TypeError("height must be an integer")
        if self.height < 0:
            raise ValueError("height must be >= 0")
