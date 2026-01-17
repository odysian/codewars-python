# https://www.codewars.com/kata/526233aefd4764272800036f/train/python

import numpy as np


# NumPy
def matrix_addition(a, b):
    return (np.array(a) + np.array(b)).tolist()


# Zip
def matrix_addition1(a, b):
    result = []

    for row_a, row_b in zip(a, b):
        new_row = []

        for val_a, val_b in zip(row_a, row_b):
            new_row.append(val_a + val_b)

        result.append(new_row)

    return result


# Nested Loop
def matrix_addition2(a, b):
    result = []
    n = len(a)
    for i in range(n):
        row = []
        for j in range(n):
            row.append(a[i][j] + b[i][j])
        result.append(row)

    return result
