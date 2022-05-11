from sys import stdin


def sol():
    dp = [[0, 0, 0] for _ in range(100001)]

    N = int(stdin.readline())
    modulo = 9901

    dp[1] = [1, 1, 1]

    for n in range(2, N + 1):
        dp[n][0] = (dp[n - 1][0] + dp[n - 1][1] + dp[n - 1][2]) % modulo
        dp[n][1] = (dp[n - 1][0] + dp[n - 1][2]) % modulo
        dp[n][2] = (dp[n - 1][0] + dp[n - 1][1]) % modulo

    return sum(dp[N]) % 9901


print(sol())
