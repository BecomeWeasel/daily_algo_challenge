from sys import stdin

N = int(stdin.readline())


def sol():

    dp = [[0 for _ in range(101)] for _ in range(20)]

    L = list(map(int, stdin.readline().split()))
    J = list(map(int, stdin.readline().split()))

    for n in range(N):
        for h in range(1, 100 + 1):
            if h - L[n] > 0:
                dp[n][h] = max(dp[n - 1][h], dp[n - 1][h - L[n]] + J[n])
            else:
                if n == 0:
                    dp[0][h] = 0
                else:
                    dp[n][h] = dp[n - 1][h]

    return max(dp[n])


print(sol())
