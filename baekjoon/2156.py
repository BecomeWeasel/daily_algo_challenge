from sys import stdin


def sol():
    N = int(stdin.readline())

    wine = [-1]

    for _ in range(N):
        wine.append(int(stdin.readline()))

    dp = [[0, 0, 0] for _ in range(N + 1)]

    dp[1] = [0, wine[1], 0]
    for i in range(2, N + 1):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = dp[i - 1][0] + wine[i]
        dp[i][2] = dp[i - 1][1] + wine[i]

    return max(dp[N])


print(sol())
