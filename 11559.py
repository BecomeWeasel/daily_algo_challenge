from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
R, C = 12, 6


# target_list는 y,x가 내림차순으로 정렬되어 있음
def boom(target_list, grid):

  # y,x가 터지면 y-1,x가 아래로 내려옴

  while len(target_list) != 0:
    y, x = target_list[0]

    # 맨 꼭대기 층이면 위에서 내려오는게 아니라 0으로 바꿔야함
    if y == 0:
      grid[y][x] = 0

    while y > 0 and grid[y][x] != 0:
      grid[y][x] = grid[y - 1][x]
      y -= 1

    del target_list[0]

  return


def move_down(board):
  i, j = 11, 5
  while j >= 0:
    cnt = 0
    while i >= 0:
      if board[i][j] == 0:
        cnt += 1
        i -= 1
        continue
      if not cnt:
        i -= 1
        continue
      board[i + cnt][j] = board[i][j]
      board[i][j] = 0
      i += cnt
      cnt = 0
    j -= 1
    i = 11


def bfs(grid, check, q):
  target_list = list()

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

  return sorted(target_list, key=lambda x: (x[0], x[1]))


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
            boom_list.append(target_list)

    move_down(grid)

    if not is_boom:
      return chain

    # if len(boom_list) == 0:
    #   return chain

    # for PUYO in boom_list:
    #   boom(PUYO, grid)

    chain += 1


print(sol())