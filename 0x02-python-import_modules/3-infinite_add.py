#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv)
    add = 0

    for i in range(1, arg_len):
        add += int(argv[i])
    print("{:d}".format(add))
