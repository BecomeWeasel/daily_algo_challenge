from sys import stdin
from collections import deque

N = int(stdin.readline())
count = 0
grid = [[0] * (N + 1) for _ in range(N + 1)]
dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(3)]

for i in range(1, N + 1):
    grid[i] = list(map(int, stdin.readline().split()))
    grid[i].insert(0, -1)


def ans():
    global dp, grid

    dp[0][1][2] = 1

    for i in range(1, N + 1):
        for j in range(2, N + 1):
            if grid[i][j] == 1:
                continue

            dp[0][i][j] += dp[0][i][j - 1] + dp[2][i][j - 1]

            dp[1][i][j] += dp[2][i - 1][j] + dp[1][i - 1][j]

            if grid[i][j - 1] == 1 or grid[i - 1][j] == 1:
                continue
            dp[2][i][j] += dp[2][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[0][i - 1][j - 1]

    return dp[0][N][N] + dp[1][N][N] + dp[2][N][N]


print(ans())
