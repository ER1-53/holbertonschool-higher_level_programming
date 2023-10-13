#!/usr/bin/python3
"""
It's class Rectangle for creat a rectangle.
"""


class Rectangle:

    """
Initializes a new Rectangle.
Args:
- width (int): The width of the rectangle (default is 0).
- height (int): The height of the rectangle (default is  0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area_result = self.__width * self.__height
        return area_result

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perim_result = 0
        else:
            perim_result = (self.__width + self.__height) * 2
        return perim_result

    def __str__(self):
        rectangle_string = ""
        if self.__width > 0 and self.__height > 0:
            for row in range(self.__height):
                if row > 0:
                    rectangle_string += "\n"
                for element in range(self.__width):
                    rectangle_string += str(self.print_symbol)
        return rectangle_string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print(f"Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
