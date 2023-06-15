#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_keys = sorted(a_dictionary.keys())
    for i in new_keys:
        print(f"{i:s}: {a_dictionary.get(i)}")
