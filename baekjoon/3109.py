from sys import stdin

dy = [-1, 0, 1]
dx = [1, 1, 1]


def sol():
    R, C = map(int, stdin.readline().split())

    board = []

    for _ in range(R):
        board.append(list(stdin.readline().rstrip()))

    count = 0

    def OOB(y, x):
        nonlocal board
        if not (0 <= y < R) or not (0 <= x < C):
            return True
        if board[y][x] == 'x':
            return True
        return False

    visit = [[False for _ in range(C)] for _ in range(R)]
    check = [False for _ in range(R)]

    def dfs(y, x, num):
        nonlocal board, visit, count, check

        if check[num]:
            return

        if x == C - 1:
            count += 1
            check[num] = True
            return

        for k in range(3):
            ny, nx = y + dy[k], x + dx[k]

            if OOB(ny, nx):
                continue

            if not visit[ny][nx] and not check[num]:
                # board[ny][nx]='x'
                visit[ny][nx]=True
                dfs(ny, nx, num)

    for y in range(R):
        # visit.add((y, 0))
        visit[y][0]=True
        dfs(y, 0, y)

    # print(check)

    return count


print(sol())