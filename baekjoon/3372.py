from sys import stdin
from collections import deque


def ans():
    global dp
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                break

            ny = grid_map[i][j] + i
            if ny < N:
                dp[ny][j] += dp[i][j]

            nx = grid_map[i][j] + j
            if nx < N:
                dp[i][nx] += dp[i][j]

    return dp[N - 1][N - 1]


grid_map = [[0] * 100 for _ in range(100)]
N = int(stdin.readline())
for i in range(N):
    grid_map[i] = list(map(int, stdin.readline().split()))

dp = [[0] * 100 for _ in range(100)]
print(ans())
