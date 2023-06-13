#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len < 1:
        first_alp = None
    else:
        first_alp = sentence[0]
    tup = (str_len, first_alp)
    return tup
