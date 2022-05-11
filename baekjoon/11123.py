from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if ny <= 0 or nx <= 0 or ny > h or nx > w:
                continue

            if not visited[ny][nx] and grid[ny][nx] == 1:
                q.append((ny, nx))
                visited[ny][nx] = True


for _ in range(int(sys.stdin.readline())):
    cnt = 0
    h, w = map(int, sys.stdin.readline().split())

    grid = [[0] * 101 for _ in range(100 + 1)]
    visited = [[False] * (w + 1) for _ in range(h + 1)]

    for i in range(1, h + 1):
        s = sys.stdin.readline()
        for j in range(1, w + 1):
            if s[j - 1] == "#":
                grid[i][j] = 1
            else:
                grid[i][j] = 0

    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                bfs(i, j)
                cnt += 1
    print(cnt)
