#!/usr/bin/python3
'''Pascal triangle
'''


def pascal_triangle(n):
    '''Generate Pascal's Triangle up to the nth row.
    '''
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1,1]]
    else:
        pascal = [[1], [1,1]]
        for i in range(2, n):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            row.append(1)
            pascal.append(row)
        return pascal