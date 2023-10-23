#!/usr/bin/python3
"""Rectangle of the project"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        
        attributes = ["width", "height", "x", "y"]

        for attr in attributes:
            value = locals()[attr]
            if not isinstance(value, int):
                raise TypeError(f"{attr} must be an integer")
            elif (attr == "width" or attr == "height") and value <= 0:
                raise ValueError(f"{attr} must be > 0")
            elif (attr == "y" or attr == "x") and value < 0:
                raise ValueError(f"{attr} must be >= 0")
   

        @property
        def width(self):
            return self.__width
        
        @width.setter
        def width(self, value):
            self.__width = value
            return value
        
        @property
        def height(self):
            return self.__height
        @height.setter
        def height(self, value):
            self.__height = value
            return value
        
        @property
        def x(self):
            return self.__x
        @x.setter
        def x(self, value):
            self.__x = value
            return value
        
        @property
        def y(self):
            return self.__y
        @y.setter
        def y(self, value):
            self.__y = value
            return value