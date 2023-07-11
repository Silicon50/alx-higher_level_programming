#!/usr/bin/python3

""" my first inderitance project"""

class Mylist(list):
	""" a method that print a list"""
	def __init__(self):
		super().__init__()
	
	def print_sorted(self):
		""" printing the sorted list"""
		print(sorted(self))
