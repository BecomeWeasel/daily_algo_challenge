from sys import stdin

N = int(stdin.readline())


def sol():

    dp = [[float('inf'), float('inf'), float('inf'), float('inf')] for _ in range(1000 + 1)]

    R, G, B = [0 for _ in range(1000 + 1)], [0 for _ in range(1000 + 1)], [0 for _ in range(1000 + 1)]

    for i in range(1, N + 1):
        r, g, b = map(int, stdin.readline().split())
        R[i], G[i], B[i] = r, g, b

    dp[1][1] = R[1]
    dp[1][2] = G[1]
    dp[1][3] = B[1]

    for i in range(2, N + 1):
        dp[i][1] = min(dp[i - 1][2], dp[i - 1][3]) + R[i]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][3]) + G[i]
        dp[i][3] = min(dp[i - 1][1], dp[i - 1][2]) + B[i]

    return min(dp[N])


print(sol())