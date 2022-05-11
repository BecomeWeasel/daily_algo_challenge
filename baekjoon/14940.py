from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def ans():
    bfs(start_y, start_x)
    # print('\n\n')
    for i in range(n):
        s = ""
        for j in range(m):
            if grid[i][j] == 0:
                s += str(0) + " "
            else:
                s += str(dist_grid[i][j]) + " "
        print(s)


def bfs(start_y, start_x):
    q = deque()
    q.append((start_y, start_x, 0))

    visited[start_y][start_x] = True

    while q:
        y, x, dist = q.popleft()

        dist_grid[y][x] = dist

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if not visited[ny][nx] and grid[ny][nx] == 1:
                q.append((ny, nx, dist + 1))
                visited[ny][nx] = True


n, m = map(int, stdin.readline().split())
start_x, start_y = 0, 0

visited = [[False] * m for _ in range(n)]
grid = [[0] * m for _ in range(n)]

for i in range(n):
    grid[i] = list(map(int, stdin.readline().split()))

dist_grid = [[-1] * (m) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start_y, start_x = i, j

ans()
