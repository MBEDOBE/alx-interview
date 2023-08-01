#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.
"""
import sys


def initialize_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty cells."""
    chessboard = []
    [chessboard.append([' ' for _ in range(n)]) for _ in range(n)]
    return chessboard


def chessboard_deepcopy(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(chessboard_deepcopy, chessboard))
    return chessboard


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard)):
            if chessboard[row][col] == "Q":
                solution.append([row, col])
                break
    return solution


def mark_unavailable_spots(chessboard, row, col):
    """Mark spots on a chessboard where non-attacking queens can no longer be placed."""
    n = len(chessboard)

    # Mark all spots in the same row as 'x'
    for c in range(n):
        chessboard[row][c] = 'x'

    # Mark all spots in the same column as 'x'
    for r in range(n):
        chessboard[r][col] = 'x'

    # Mark all spots in the diagonals as 'x'
    for i in range(n):
        if row + i < n and col + i < n:
            chessboard[row + i][col + i] = 'x'
        if row - i >= 0 and col - i >= 0:
            chessboard[row - i][col - i] = 'x'
        if row + i < n and col - i >= 0:
            chessboard[row + i][col - i] = 'x'
        if row - i >= 0 and col + i < n:
            chessboard[row - i][col + i] = 'x'


def recursive_solve(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    n = len(chessboard)

    if queens == n:
        solutions.append(get_solution(chessboard))
        return solutions

    for col in range(n):
        if chessboard[row][col] == ' ':
            tmp_chessboard = chessboard_deepcopy(chessboard)
            tmp_chessboard[row][col] = 'Q'
            mark_unavailable_spots(tmp_chessboard, row, col)
            solutions = recursive_solve(
                tmp_chessboard, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
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
    chessboard = initialize_chessboard(N)
    solutions = recursive_solve(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
