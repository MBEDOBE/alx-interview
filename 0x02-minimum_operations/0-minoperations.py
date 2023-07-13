#!/usr/bin/python3

"""
    Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: n: Number of characters to be displayed
        return:
               number of min operations
    """

    current = 1
    initial = 0
    count = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            initial = current
            current += initial
            count += 2
        else:
            current += initial
            count += 1
    return count
