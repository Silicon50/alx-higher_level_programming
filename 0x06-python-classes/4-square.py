#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.
        """
        self.size = size

    @property
    def size(self):
        """Get size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area"""
        return self.__size ** 2
