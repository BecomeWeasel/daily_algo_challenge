from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():
    N, M = map(int, stdin.readline().split())

    board = [['A' for _ in range(M)] for _ in range(N)]

    for i in range(N):
        s = stdin.readline()

        for j in range(M):
            if s[j] == 'U':
                board[i][j] = 0
            elif s[j] == 'D':
                board[i][j] = 1
            elif s[j] == 'L':
                board[i][j] = 2
            elif s[j] == 'R':
                board[i][j] = 3

    count = 0

    dp = [[-1 for _ in range(M)] for _ in range(N)]

    def dfs(y, x, check):
        nonlocal board, N, M, count

        # 이미 탈출가능한 루트의 일부분일때 (탈출가능한 외곽 포함)
        if dp[y][x] != -1:
            return dp[y][x]

        # 보드에 적혀잇는 다음 위치로
        ny, nx = y + dy[board[y][x]], x + dx[board[y][x]]

        # 지금 현재 위치에서 탈출 가능하면
        if not (0 <= ny < N and 0 <= nx < M):
            dp[y][x] = 1
            return dp[y][x]

        # 이 루트는 사이클이 생긴다 그러니까 탈출불가
        if (ny, nx) in check:
            dp[y][x] = 0
            return 0
        else:
            check.add((ny, nx))

            dp[y][x] = dfs(ny, nx, check)

            return dp[y][x]

    for i in range(N):
        for j in range(M):
            dp[i][j] = dfs(i, j, {(i, j)})
            if dp[i][j] == 1:
                count += 1

    return count


print(sol())