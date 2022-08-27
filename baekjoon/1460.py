from sys import stdin

N, M = map(int, stdin.readline().split())

board = [[0 for _ in range(N)] for _ in range(N)]


for _ in range(M):
    x, y, l, f = map(int, stdin.readline().split())

    for i in range(y, y + l):
        for j in range(x, x + l):
            board[i][j] = f

answer = 0

for first in range(1, 8):
    for second in range(first, 8):
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            dp[0][i] = 1 if (board[0][i] == first or board[0][i] == second) else 0

        for i in range(N):
            dp[i][0] = 1 if (board[i][0] == first or board[i][0] == second) else 0

        for i in range(1, N):
            for j in range(1, N):
                if board[i][j] == first or board[i][j] == second:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    answer = max(answer, dp[i][j])
print(answer**2)


# for r in board:
#     print(r)
