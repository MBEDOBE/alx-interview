#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.
"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

N = int(sys.argv[1])


def find_queen_positions(n, i=0, col_set=set(), diag_sum_set=set(), diag_diff_set=set()):
    """Find possible positions for the queens."""
    if i < n:
        for j in range(n):
            if j not in col_set and i + j not in diag_sum_set and i - j not in diag_diff_set:
                yield from find_queen_positions(n, i + 1, col_set | {j}, diag_sum_set | {i + j}, diag_diff_set | {i - j})
    else:
        yield list(col_set)


def solve(n):
    """Solve and print the solutions."""
    solution_count = 0
    for solution in find_queen_positions(n, 0):
        k = []
        for i, col in enumerate(solution):
            k.append([i, col])
        print(k)
        solution_count += 1

    print(f"Total solutions: {solution_count}")


solve(N)
