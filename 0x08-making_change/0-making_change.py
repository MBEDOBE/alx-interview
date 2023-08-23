#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total"""


#!/usr/bin/python3

def makeChange(coins, total):
    """This function will take a list of coins and use
       that to calculate how much change the total will require
    """
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
