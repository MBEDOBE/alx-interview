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

    """ now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter """

    if n == 1:
        return 0

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    operations = 0
    count = 0
    prev_factor = 0

    for factor in factors:
        if factor == prev_factor:
            count += 1
        else:
            count = 1
            prev_factor = factor

        if count == 1:
            operations += 2
        elif count == 2:
            operations += 1

    return operations
