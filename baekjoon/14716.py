from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0, -1, 1, 1, -1]
dx = [0, 0, -1, 1, -1, -1, 1, 1]


def ans():
  cnt = 0

  for i in range(N):
    for j in range(M):
      if grid[i][j] == 1 and not visited[i][j]:
        bfs(i, j)
        cnt += 1
        visited[i][j] = True

  return cnt


def bfs(i, j):
  q = deque()
  q.append((i, j))

  while q:
    y, x = q.popleft()

    for k in range(8):
      ny = y + dy[k]
      nx = x + dx[k]

      if ny < 0 or nx < 0 or ny >= N or nx >= M:
        continue

      if grid[ny][nx] == 1 and not visited[ny][nx]:
        q.append((ny, nx))
        visited[ny][nx] = True

  return 0


N, M = map(int, stdin.readline().split())
grid = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
  grid[i] = list(map(int, stdin.readline().split()))

print(ans())