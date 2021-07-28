from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    dp = [[0 for _ in range(M)] for _ in range(N)]

    board = []
    for _ in range(N):
        board.append(list(map(int, stdin.readline().split())))

    dp[0][0] = board[0][0]

    def is_safe(y, x):
        if not (0 <= y < N) or not (0 <= x < M):
            return False
        return True

    for i in range(N):
        for j in range(M):
            for ny, nx in (i + 1, j), (i, j + 1):
                if is_safe(ny, nx):
                    dp[ny][nx] = max(dp[ny][nx], dp[i][j] + board[ny][nx])

    return dp[N - 1][M - 1]


print(sol())