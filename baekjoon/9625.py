from sys import stdin

K = int(stdin.readline())


def sol():
    dp = [[0, 0] for _ in range(45 + 1)]
    dp[0] = [1, 0]
    dp[1] = [0, 1]

    for n in range(2, K + 1):
        dp[n][0] = dp[n - 1][1]
        dp[n][1] = dp[n - 1][0] + dp[n - 1][1]

    return ' '.join(map(str, dp[K]))


print(sol())