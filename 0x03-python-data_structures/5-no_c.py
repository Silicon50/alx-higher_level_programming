#!/usr/bin/python3

def no_c(my_string):
    str_len = len(my_string)
    new_string = ""
    for i in range(str_len):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        new_string += my_string[i]
    my_string = new_string
    return my_string
