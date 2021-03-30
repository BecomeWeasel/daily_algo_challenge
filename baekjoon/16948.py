from sys import stdin
from collections import deque

dy = [-2, -2, 0, 0, 2, 2]
dx = [-1, 1, -2, 2, -1, 1]


def ans():
  return bfs()


def bfs():
  q = deque()
  q.append((start_y, start_x, 0))
  visited[start_y][start_x] = True
  while q:
    ypos, xpos, cnt = q.popleft()

    if ypos == end_y and xpos == end_x:
      return cnt

    for k in range(6):
      ny = ypos + dy[k]
      nx = xpos + dx[k]

      if ny >= N or nx >= N or ny < 0 or nx < 0:
        continue

      if not visited[ny][nx]:
        visited[ny][nx] = True
        q.append((ny, nx, cnt + 1))

  return -1


N = int(stdin.readline())
start_y, start_x, end_y, end_x = map(int, stdin.readline().split())
visited = [[False] * N for _ in range(N)]
print(ans())