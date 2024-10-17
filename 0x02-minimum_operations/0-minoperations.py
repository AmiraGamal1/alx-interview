#!/usr/bin/python3
'''Coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 4:
        return 4
    if n % 2 == 0:
        if n % 4 == 0:
            return (n // 4 + 4 )
        else:
            return (n // 2 + 2)
    else:
        return 0