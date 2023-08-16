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
        
	@property
	def size(self):
        """getting the value of size"""
        return self.__size
    
	@size.getter
    def size(self, value):
        """setting the value of size"""
        if type(value) is not int:
            raise TypeError("Value must be integer")
        if value < 0:
            raise ValueError("Value must be greater than 0")
        self.__size = value
    def my_print(self):
        if self.size == 0:
            print()
        for i in range(0, self.size):
            print('#' * self.size)
            print()
            

         