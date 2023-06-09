#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    arg_len = len(argv)
    real_len = arg_len - 1

    if real_len == 0:
        print("0 arguments.")
    elif real_len == 1:
        print("1 argument:\n1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(real_len))
        for i in range(1, arg_len):
            print("{:d}: {:s}".format(i, argv[i]))
