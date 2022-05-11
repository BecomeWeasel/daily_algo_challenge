from sys import stdin

N = int(stdin.readline())


def sol():
    dp = [[0, 0] for _ in range(91)]

    dp[1] = [0, 1]
    dp[2] = [1, 0]

    for n in range(3, N + 1):
        dp[n][0] = dp[n - 1][0] + dp[n - 1][1]
        dp[n][1] = dp[n - 1][0]

    return sum(dp[N])


print(sol())
