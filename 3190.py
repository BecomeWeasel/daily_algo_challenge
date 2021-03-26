from sys import stdin
from collections import deque

# 방위
N, E, S, W = 0, 1, 2, 3

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board_size = int(stdin.readline())
K = int(stdin.readline())


def sol():
  # 1,1부터 N,N까지
  grid = [[0] * (board_size + 1) for _ in range(board_size + 1)]
  for _ in range(K):
    y, x = map(int, stdin.readline().split())
    # 1은 사과가 있다는 의미
    grid[y][x] = 1

  snake = deque()
  # 초기 위치와 E를 바라보고 있음
  snake.append((1, 1, 1))
  # 2는 뱀이 있다는 뜻
  grid[1][1] = 2

  turnings = []
  # L번 동안 전환을 기록
  for _ in range(int(stdin.readline())):
    time, direct = stdin.readline().split()
    time = int(time)
    turnings.append([time, direct])

  elapsed_time = 0

  while True:

    elapsed_time += 1

    prev_dir = -1
    moved_snake = deque()
    for body in snake:
      y, x, direct = body

      # 꺾이는 방향에서
      new_direct = direct if prev_dir == -1 else prev_dir

      ny, nx, = y + dy[direct], x + dx[direct]

      # 벽을 부딪혔을때
      if ny < 1 or nx < 1 or ny > board_size or nx > board_size:
        return elapsed_time

      # 움직일곳에 뱀이 있다면
      if grid[ny][nx] == 2:
        return elapsed_time

      # 사과를 먹으면
      if grid[ny][nx] == 1:
        grid[ny][nx] = 2
        # 기존의 뱀들은 그대로 그자리에 있고
        # 머리를 앞에 붙인다고 생각
        moved_snake = snake
        moved_snake.appendleft([ny, nx, new_direct])
        prev_dir = direct
        break

      # 뱀이 이동하고
      grid[y][x] = 0
      # 새로운 위치에 뱀을 표시
      grid[ny][nx] = 2
      moved_snake.append([ny, nx, new_direct])

      prev_dir = direct

    # 이동한 뱀을 복사하기
    snake = moved_snake
    
    

    # 돌아야할 시간이라면
    # turnings는 항상 시간순서대로 정렬되어 있으므로
    # turnings[0]만 보면 됨
    if len(turnings) != 0  and elapsed_time == turnings[0][0]:
      # 왼쪽으로 돌기
      if turnings[0][1] == 'L':
        moved_snake[0][2] = comp_3((comp_3(moved_snake[0][2]) + 1) % 4)
      # 오른쪽으로 돌기
      else:
        moved_snake[0][2] = (moved_snake[0][2] + 1) % 4
      del turnings[0]

  return 1


def comp_3(num):
  return abs(3 - num)


print(sol())
