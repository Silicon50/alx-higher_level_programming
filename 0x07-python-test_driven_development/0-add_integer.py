#!/usr/bin/python3
""" A function that add two integers"""

def add_integer(a, b=98):
    """
    a function that returns two integer
    Args:
		a : first parameter must be float or int
        b : second parameter must be float or int
    raise error if a or b not int or float
    """
    if type(a) is not [int,float]:
        raise TypeError("a must be int or float")
    if type(b) is not [int, float]:
        raise TypeError("b must be int or float")
    return int(a) + int(b)