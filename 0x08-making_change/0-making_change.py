#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


def make_change(coins, total):
    """This function calculates how much change is required using a list of coins."""
    if total <= 0:
        return 0
    else:
        coins.sort(reverse=True)
        counter = 0
        for coin in coins:
            while total >= coin:
                counter += 1
                total -= coin
        if total == 0:
            return counter
        return -1


if __name__ == "__main__":
    # Example usage:
    coins = [1, 2, 5]
    total = 11
    result = make_change(coins, total)
    print(result)
