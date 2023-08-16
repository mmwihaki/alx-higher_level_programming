#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0])

    squared_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):

            squared_value = matrix[i][j] ** 2

            squared_matrix[i][j] = squared_value
    return squared_matrix
