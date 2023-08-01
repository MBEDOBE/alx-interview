#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.
"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, e=0, a=[], b=[], c=[]):
    """ find possible positions """
    if e < n:
        for j in range(n):
            if j not in a and e + j not in b and e - j not in c:
                yield from queens(n, e + 1, a + [j], b + [e + j], c + [e - j])
    else:
        yield a


def solve(n):
    """ solve """
    k = []
    e = 0
    for solution in queens(n, 0):
        for s in solution:
            k.append([e, s])
            i += 1
        print(k)
        k = []
        e = 0


solve(n)
