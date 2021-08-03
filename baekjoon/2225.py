from sys import stdin


def sol():
    N, K = map(int, stdin.readline().split())

    dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

    modulo = 1000000000

    for i in range(N + 1):
        dp[1][i] = 1

    for i in range(2, K + 1):
        for j in range(N + 1):
            for p in range(j + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) % modulo

    return dp[K][N]


print(sol())