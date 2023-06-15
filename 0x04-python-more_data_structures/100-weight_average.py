#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        w = 0
        d = 0
        average = 0
        
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                w += my_list[i][0] * my_list[i][1]
                d += my_list[i][1]
        average = w / d
        return average
    return 0
