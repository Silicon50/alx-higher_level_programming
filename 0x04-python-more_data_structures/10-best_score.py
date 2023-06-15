#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        a = list(a_dictionary)
        k = a[0]
        for i in a:
            if a_dictionary[k] < a_dictionary[i]:
                k = i
        return k
    else:
        return
