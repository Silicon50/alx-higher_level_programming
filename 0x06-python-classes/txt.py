#!/usr/bin/python3

""" A class that define a square"""
class Square():
    """Initializing the square with size"""
    def __init__(self, size = 0):
        if type(size) is not int:
            raise TypeError("Not an Integer")
        if (size < 0):
            raise ValueError("Size must be >= 0")
        self.size = size
        
	def area(self):
            """That define area of a square"""
            return self.__size ** 2
         