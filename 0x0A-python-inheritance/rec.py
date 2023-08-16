#!/usr/bin/python3
"""To find the area of a rectangle"""
class Rectangle():
    """Initalizing the rectangle"""
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width
        
    @property
    def length(self):
        print("Returning the length")
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

    @property
    def width(self):
        print("Print the width")
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    def getArea(self):
        print("{} * {} = {}".format(self.__length, self.__width, self.__length * self.__width))

class Parameter(Rectangle):
    def __init__(self, length = 0, width = 0, height = 0):
        super().__init__(length, width)
        self.height = height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value

    def getVol(self):
        print("volume = {}".format(self.length * self.width * self.__height))
rec1 = Rectangle(3,4)
print(rec1.length)
rec1.getArea()

par = Parameter(3,5,6)
#print(par.length)
#print(par.width)
#print(par.height)
#par.getVol()

print(dir(par))