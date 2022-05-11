from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

R, C = map(int, stdin.readline().split())
max_board = -1

grid = [["A"] * (C + 1) for _ in range(R + 1)]

for i in range(1, R + 1):
    alpha = stdin.readline()
    for j in range(C):
        grid[i][j + 1] = alpha[j]


def is_safe(next_char, current_str):
    for char in current_str:
        if next_char == char:
            return False
    return True


def bfs():
    global max_board
    q = deque()
    q.append((1, 1, grid[1][1], 1))

    while q:
        y, x, current_str, board = q.popleft()
        max_board = max(max_board, board)

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if ny > R or nx > C or ny < 1 or nx < 1:
                continue

            if is_safe(grid[ny][nx], current_str):
                q.append((ny, nx, current_str + grid[ny][nx], board + 1))


visited = [False for _ in range(26)]

visited[ord(grid[1][1]) - ord("A")] = True


def dfs(y, x, board):
    global max_board
    visited[ord(grid[y][x]) - ord("A")] = True

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if ny > R or nx > C or ny < 1 or nx < 1:
            continue

        if not visited[ord(grid[ny][nx]) - ord("A")]:
            dfs(ny, nx, board + 1)

    visited[ord(grid[y][x]) - ord("A")] = False
    max_board = max(max_board, board)


# bfs()
dfs(1, 1, 1)
print(max_board)
