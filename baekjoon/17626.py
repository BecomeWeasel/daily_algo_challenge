from sys import stdin
from math import sqrt

N = int(stdin.readline())


def sol() -> int:
    dp = [float('inf') for _ in range(50000 + 1)]

    dp[1] = 1
    dp[2] = 2

    for i in range(1, int(sqrt(50001))):
        dp[i * i] = 1

    for n in range(3, N+1):
        for x in range(int(sqrt(n)+1)):
            dp[n] = min(dp[n], dp[n - x * x] + 1)

    return dp[n]


print(sol())