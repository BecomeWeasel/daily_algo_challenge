from sys import stdin


def sol():
    N, M = map(int, stdin.readline().split())

    board = []

    for _ in range(N):
        board.append(list(map(int, stdin.readline().split())))

    def OOB(y, x):
        if not (0 <= y < N) or not (0 <= x < M):
            return True
        return False

    dp = [[-1 for _ in range(M)] for _ in range(N)]

    def recur(y, x):
        nonlocal board

        if OOB(y, x):
            return 0

        if dp[y][x] != -1:
            return dp[y][x]

        dp[y][x] = max(recur(y - 1, x - 1), recur(y - 1, x), recur(y, x - 1)) + board[y][x]

        return dp[y][x]

    return recur(N - 1, M - 1)


print(sol())
