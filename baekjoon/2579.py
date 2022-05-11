from sys import stdin

N = int(stdin.readline())


def sol():
    dp = [[0 for _ in range(3)] for _ in range(300 + 1)]

    point = [0 for _ in range(301)]
    for i in range(N):
        point[i + 1] = int(stdin.readline())

    dp[1][1] = point[1]
    dp[2][1] = point[2]
    dp[2][2] = point[1] + point[2]

    for n in range(3, N + 1):
        dp[n][1] = max(dp[n - 2]) + point[n]
        dp[n][2] = dp[n - 1][1] + point[n]

    return max(dp[N])


print(sol())
