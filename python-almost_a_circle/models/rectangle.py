#!/usr/bin/python3
"""Rectangle of the project"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """if not isinstance(width, int):
        raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")"""

        super().__init__(id)

        attributes = ["width", "height", "x", "y"]

        for attr in attributes:
            value = locals()[attr]
            if not isinstance(value, int):
                raise TypeError(f"{attr} must be an integer")
            elif (attr == "width" or attr == "height") and value <= 0:
                raise ValueError(f"{attr} must be > 0")
            elif (attr == "y" or attr == "x") and value < 0:
                raise ValueError(f"{attr} must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        """for row in range(self.__height):
            for element in range(self.__width):
                print("#", end='')
            print()"""
        """for row in range(self.__height):
            print("".join(["#" for _ in range(self.__width)]))"""
        for y in range(self.y):
            print()
        for row in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """Display informations"""
        class_name = self.__class__.__name__
        id = self.id
        w = self.width
        h = self.height
        # adaptation for pystylecode
        return f"[{class_name}] ({id}) {self.x}/{self.y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """Update all attribut """
        attribute_names = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for i in range(min(len(args), len(attribute_names))):
                setattr(self, attribute_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
