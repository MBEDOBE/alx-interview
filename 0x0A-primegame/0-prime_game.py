#!/usr/bin/python3

def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        if n % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winner_count = {"Maria": 0, "Ben": 0}

    for n in nums:
        if is_prime(n):
            winner = play_game(n)
            winner_count[winner] += 1

    if winner_count["Maria"] > winner_count["Ben"]:
        return "Maria"
    elif winner_count["Ben"] > winner_count["Maria"]:
        return "Ben"
    else:
        return None


# Example usage
if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    result = isWinner(x, nums)
    print(result)  # Output: "Ben"
