#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
	n = len(argv)
	arg = n - 1

	if arg == 0:
		print("0 arguments.")
	elif arg == 1:
		print("1 argument:\n1: {:s}".format(argv[1]))
	else:
		print("{:d} arguments:".format(arg))
	for i in range(1, n):
		print("{:d}: {:s}".format(i, argv[i]))
