from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 불을 번지게 하기
# 인자로 들어온 fire_q안에는 초기 불의 위치가 적혀있음
def spread_fire(w, h, grid, fire_q, fire_time):
  check = [[False] * (w + 1) for _ in range(h + 1)]

  while fire_q:
    y, x, time = fire_q.popleft()

    if not check[y][x]:
      check[y][x]=True

    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]

      if ny > h or nx > w or ny < 1 or nx < 1:
        continue

      # 벽이 아니거나 같은 불이 아니면
      if not check[ny][nx] and grid[ny][nx] != '#' and grid[ny][nx] != '*':
        check[ny][nx] = True
        fire_time[ny][nx] = time + 1
        fire_q.append((ny, nx, time + 1))

  # print()
  # for i in range(1, h + 1):
  #   s = ""
  #   for j in range(1, w + 1):
  #     s += str(fire_time[i][j]==9999 and "N" or fire_time[i][j]) + " "
  #   print(s)

  # print()
  # for i in range(1, h + 1):
  #   s = ""
  #   for j in range(1, w + 1):
  #     s += grid[i][j] + " "
  #   print(s)


def ans(w, h, grid, start_y, start_x, fire_q, fire_time):
  # q.append((start_y, start_x))
  q = deque()
  q.append((start_y, start_x))
  time = 0

  spread_fire(w, h, grid, fire_q, fire_time)

  while True:
    move_q = deque()

    if not q:
      print("IMPOSSIBLE")
      return

    while q:
      y, x = q.popleft()


      # 끝줄에 도착했다면
      if y == h or y == 1 or x == w or x == 1:
        print(time + 1)
        return

      for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if ny > h or nx > w or ny < 1 or nx < 1:
          continue

        # 방문하지 않았거나 빈 칸이고
        # 방문했을 시간에 아직 불이 붙지 않았다면
        if not check[ny][nx] and grid[ny][nx] == '.' and time+1 < fire_time[ny][nx]:
          move_q.append((ny, nx))
          check[ny][nx] = True

    while move_q:
      q.append(move_q.popleft())

    time += 1


T = int(stdin.readline())
# w, h = 0, 0
while T:
  # global w, h
  w, h = map(int, stdin.readline().split())
  start_y, start_x = 0, 0
  fire_q = deque()

  grid = [['#'] * (w + 1) for _ in range(h + 1)]
  fire_time = [[9999] * (w + 1) for _ in range(h + 1)]
  check = [[False] * (w + 1) for _ in range(h + 1)]

  for i in range(1, h + 1):
    input_list = stdin.readline()
    for j in range(w):
      grid[i][j + 1] = input_list[j]
      if grid[i][j+1] == '@':
        start_y, start_x = i, j + 1
      elif grid[i][j+1] == '*':
        fire_q.append((i, j+1, 0))
        fire_time[i][j+1] = 0
  ans(w, h, grid, start_y, start_x, fire_q, fire_time)
  T -= 1
