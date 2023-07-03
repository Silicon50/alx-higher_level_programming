#!/usr/bin/python3
"""using # to print a rectangle"""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
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
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """to print rectangle"""
        p_rect = ""
        if self.__width == 0 or self.__height == 0:
            return p_rect

        for length in range(self.__height):
            for size in range(self.__width):
                p_rect = p_rect + '#'
            if length != self.__height - 1:
                p_rect = p_rect + '\n'
        return 
