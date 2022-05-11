from sys import stdin


def sol():
    H, Y = map(int, stdin.readline().split())

    dp = [0 for _ in range(30)]
    dp[0] = H
    dp[1] = int(1.05 * H)

    for n in range(0, Y):
        dp[n + 1] = max(dp[n + 1], int(1.05 * dp[n]))
        dp[n + 3] = max(dp[n + 3], int(1.2 * dp[n]))
        dp[n + 5] = max(dp[n + 5], int(1.35 * dp[n]))

    return dp[Y]


print(sol())
