from sys import stdin, stdout

N = int(stdin.readline())


def sol():
    dp = [0 for _ in range(int(1e6) + 1)]

    dp[1] = 1
    dp[2] = 2

    for n in range(3, N + 1):
        dp[n] = (dp[n - 1] + dp[n - 2])%15746

    return dp[N]


print(sol())