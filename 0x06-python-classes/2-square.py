#!/usr/bin/python3
"""A square based on 1-square.py"""

class Square:
    """Instantiation to raise both TypeError and ValueError when applicable"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
