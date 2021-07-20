from sys import stdin

N = int(stdin.readline())


def sol():
    global N

    board = []

    for _ in range(N):
        board.append(list(map(int, stdin.readline().split())))

    dp = [[0 for _ in range(N)] for _ in range(N)]

    def safe(y, x):
        global N
        if not (0 <= y < N) or not (0 <= x < N):
            return False
        return True

    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if i == N - 1 and j == N - 1:
                continue
            dist = board[i][j]

            if safe(i + dist, j):
                dp[i + dist][j] += dp[i][j]

            if safe(i, j + dist):
                dp[i][j + dist] += dp[i][j]

    return dp[N - 1][N - 1]


print(sol())