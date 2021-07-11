from sys import stdin

N = int(stdin.readline())


def sol():
    dp = [0 for _ in range(100000 + 1)]

    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    dp[6] = 3
    dp[7] = 2
    dp[8] = 4

    for n in range(9, N + 1):
        dp[n] = min(dp[n - 2], dp[n - 5]) + 1

    # print(dp[:20])

    return dp[N] if dp[N] != 0 else -1


print(sol())