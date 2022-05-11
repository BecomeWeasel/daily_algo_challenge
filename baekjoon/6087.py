from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():
    W, H = map(int, stdin.readline().split())

    board = []

    def OOB(y, x):
        if not (0 <= y < H) or not (0 <= x < W):
            return True
        return False

    for _ in range(H):
        board.append(list(stdin.readline().rstrip()))

    p_y, p_x = None, None
    e_y, e_x = None, None
    for i in range(H):
        for j in range(W):
            if board[i][j] == "C":
                if p_y != None:
                    e_y, e_x = i, j
                else:
                    p_y, p_x = i, j

    q = deque()
    q.append((p_y, p_x, -1, 0))
    visit = [[float("inf") for _ in range(W)] for _ in range(H)]
    visit[p_y][p_x] = 0

    while q:
        y, x, prev, mirror = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if OOB(ny, nx):
                continue

            if board[ny][nx] == "*":
                continue

            # 방향 전환이 필요하고 더 적은 거울개수가 필요하면

            # visit[y][x]를 사용하면 값이 덮어씌워지는 dirty value 문제가 있음
            # if prev != k and visit[y][x] + 1 <= visit[ny][nx]:
            if prev != k and mirror + 1 <= visit[ny][nx]:
                visit[ny][nx] = mirror + 1
                q.append((ny, nx, k, mirror + 1))

            elif prev == k and mirror <= visit[ny][nx]:
                visit[ny][nx] = mirror
                q.append((ny, nx, k, mirror))

    return visit[e_y][e_x] - 1


print(sol())
