#!/usr/bin/python3

for first in range(0, 10):
    for sec in range(1, 10):
        if first >= sec:
            continue
        if first == 8 and sec == 9:
            print("{}{}".format(first, sec))
        else:
            print("{}{}".format(first, sec), end=", ")

