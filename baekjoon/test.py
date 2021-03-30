from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
R, C = 12, 6


def gravity(grid):

  for x in range(C):
    for y in range(R - 1, -1, -1):
      if grid[y][x] == 0:
        continue
      for k in range(R - 1, y - 1, -1):
        if grid[k][x] == 0:
          grid[k][x], grid[y][x] = grid[y][x], 0

  return


def bfs(grid, check, q):
  target_list = deque()

  while len(q) != 0:
    y, x = q.popleft()
    target_list.append((y, x))

    for k in range(4):
      ny, nx = y + dy[k], x + dx[k]

      if ny == R or nx == C or ny < 0 or nx < 0:
        continue

      # 방문하려는곳이 출발지와 같은 색이고 방문하지 않았다면
      if grid[ny][nx] == grid[y][x] and not check[ny][nx]:
        check[ny][nx] = True
        q.append((ny, nx))

  return deque(sorted(target_list, key=lambda x: (x[0], x[1])))


def sol():

  grid = []
  for _ in range(R):
    string = stdin.readline().rstrip('\n')
    row = []
    for char in string:
      if char == '.':
        row.append(0)
      elif char == 'R':
        row.append(1)
      elif char == 'G':
        row.append(2)
      elif char == 'B':
        row.append(3)
      elif char == 'P':
        row.append(4)
      elif char == 'Y':
        row.append(5)
    grid.append(row)

  chain = 0

  while True:

    check = [[False] * C for _ in range(R)]

    boom_list = []
    is_boom = False
    for i in range(R):
      for j in range(C):
        if grid[i][j] != 0 and not check[i][j]:
          check[i][j] = True
          q = deque()
          q.append((i, j))
          target_list = bfs(grid, check, q)

          if len(target_list) >= 4:
            is_boom = True
            for y, x in target_list:
              grid[y][x] = 0

    if not is_boom:
      return chain

    gravity(grid)

    chain += 1


print(sol())