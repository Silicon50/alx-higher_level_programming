#!/usr/bin/python3


def uppercase(str):
    up_case = ''
    for alp in str:
        if ord(alp) >= 97 and ord(alp) <= 122:
            up_case =up_case + chr(ord(alp) - 32)
        else:
            up_case = up_case + alp
    print("{0:s}".format(up_case))
