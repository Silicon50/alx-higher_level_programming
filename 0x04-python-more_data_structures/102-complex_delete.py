#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keylist = []
    if value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if value == val:
                keylist.append(key)

        for k in keylist:
            if k in a_dictionary:
                del a_dictionary[k]
    return a_dictionary
