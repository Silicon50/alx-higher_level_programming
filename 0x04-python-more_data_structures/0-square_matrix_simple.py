#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    new_row = []
    for row in matrix:
        for i in row:
            new_row.append(i * i)
        new_matrix.append(new_row)
        new_row = []

    return new_matrix
