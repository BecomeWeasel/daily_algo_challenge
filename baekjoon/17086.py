from sys import stdin
from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def bfs(start_y, start_x):
  global N, M, grid, safe_dist
  q = deque()
  check = [[False] * (M + 1) for _ in range(N + 1)]
  q.append((start_y, start_x, 0))
  check[start_y][start_x] = True

  while q:
    y, x, dist = q.popleft()

    for k in range(8):
      ny, nx = y + dy[k], x + dx[k]

      if ny > N or nx > M or ny < 1 or nx < 1:
        continue

      if not check[ny][nx]:
        q.append((ny, nx, dist + 1))
        check[ny][nx] = True
        safe_dist[ny][nx] = min(safe_dist[ny][nx], dist + 1)


N, M = map(int, stdin.readline().split())
grid = [[0] * (M + 1) for _ in range(N + 1)]
safe_dist = [[987654321] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  input_list = list(map(int, stdin.readline().split()))
  for j in range(M):
    grid[i][j + 1] = input_list[j]


def ans():
  for i in range(1, N + 1):
    for j in range(1, M + 1):
      if grid[i][j] == 1:
        bfs(i, j)

  max_value = 0

  for i in range(1, N + 1):
    for j in range(1, M + 1):
      if grid[i][j] != 1:
        max_value = max(max_value, safe_dist[i][j])

  return max_value


print(ans())