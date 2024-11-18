#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    n = len(matrix[0])
    for i in range(n):
        for j in range(i+1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for row in matrix:
        row.reverse()
