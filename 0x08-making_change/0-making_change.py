#!/usr/bin/python3
"""A function to determine the fewest number of coins needed to meet a given amount total"""
def makeChange(coins, total):
    if total < 0:
        return -1
    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


if __name__ == "__main__":
    # Example usage:
    coins = [1, 2, 5]
    total = 11
    result = makeChange(coins, total)
    print(result)
