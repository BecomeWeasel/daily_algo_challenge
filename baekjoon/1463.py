from sys import stdin


def ans():
    dp = [0 for _ in range(N + 1)]

    dp[1] = 0

    for num in range(2, N + 1):
        if num % 6 == 0:
            dp[num] = min(dp[num // 2], dp[num // 3], dp[num - 1]) + 1
        elif num % 2 == 0:
            dp[num] = min(dp[num // 2], dp[num - 1]) + 1
        elif num % 3 == 0:
            dp[num] = min(dp[num // 3], dp[num - 1]) + 1
        else:
            dp[num] = dp[num - 1] + 1

    return dp[N]


N = int(stdin.readline())
print(ans())
