from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# n은 세로의 길이
# m은 가로의 길이
n, m = map(int, stdin.readline().split())
grid = [[0] * (m + 1) for _ in range(n + 1)]
start_y = start_x = 0
# visit = set()
visit = [[False] * 3001 for _ in range(3001)]

for i in range(n):
  s = stdin.readline().rstrip("\n")
  for j in range(len(s)):
    grid[i + 1][j + 1] = int(s[j])
    if int(s[j]) == 2:
      start_y = i + 1
      start_x = j + 1


def ans():
  bfs()


def bfs():
  q = deque()
  q.append((start_y, start_x, 0))
  # visit.add((start_y, start_x))
  visit[start_y][start_x]=True

  while q:
    y, x, dist = q.popleft()

    # if grid[y][x] != 0 and grid[y][x]!=2:
    #   print("TAK")
    #   print(dist)
    #   return

    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]

      if ny > n or nx > m or ny < 1 or nx < 1:
        continue

      if not visit[ny][nx] and grid[ny][nx] != 1:
        if grid[ny][nx] != 0 and grid[ny][nx] != 2:
          print("TAK")
          print(dist + 1)
          return
        else:
          # visit.add((ny, nx))
          visit[ny][nx]=True
          q.append((ny, nx, dist + 1))

  print("NIE")


ans()
