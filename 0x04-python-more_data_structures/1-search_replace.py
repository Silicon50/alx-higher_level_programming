#!/usr/bin/python3

def search_replace(my_list, search, replace):chmo
    sec_list = my_list.copy()

    for i in range(0, len(sec_list)):
        if sec_list[i] == search:
            sec_list[i] = replace

    return sec_list
