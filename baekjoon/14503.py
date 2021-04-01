from sys import stdin

N, M = map(int, stdin.readline().split())

clean_score = 0

NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3

# N,E,S,W 방향으로 한칸 움직였을때 좌표방향
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 현재 바라보고 있는 방향이 N,E,S,W일때
# 후진할때 좌표방향
rdy = [1, 0, -1, 0]
rdx = [0, -1, 0, 1]

clean = [[False for _ in range(M)] for _ in range(N)]

board = []


def clean_floor(y, x, clean):
  global clean_score
  clean[y][x] = True
  clean_score += 1


# 현재 방향을 기준으로 좌회전하는 방향의 값을 반환
def get_left_direction_by_current_direction(direction):
  return (direction + 3) % 4


def is_no_clean(y, x):
  global clean, board
  is_no_clean = True

  # 네 방향을 탐색하면서 한칸이라도 벽이 아닌데 청소가 안 되어있는곳을 찾으려함
  for k in range(4):
    ny, nx = y + dy[k], x + dx[k]

    if 0 <= ny < N and 0 <= nx < M:
      # 벽이 아닌데 청소가 안되어있다면
      if board[ny][nx] == 0 and not clean[ny][nx]:
        is_no_clean = False

  return is_no_clean


def sol():
  y, x, direction = map(int, stdin.readline().split())

  for _ in range(N):
    board.append(list(map(int, stdin.readline().split())))

  # 일단 현재 입력받은 위치를 청소한다
  clean_floor(y, x, clean)

  while True:

    # 현재 방향 기준으로 왼쪽 방향구하기
    new_direction = get_left_direction_by_current_direction(direction)
    # 왼쪽 방향으로 한칸 움직였을때의 좌표 (ny,nx)
    ny, nx = y + dy[new_direction], x + dx[new_direction]
    # 현재 방향에서 한칸 뒤로 갔을때의 좌표 (ry,rx) 단, 이때 방향은 유지된다
    ry, rx = y + rdy[direction], x + rdx[direction]

    # 왼쪽방향이 청소가 안되어 있고 그곳이 벽이 아니라면
    # 그쪽으로 회전한후 움직이고 그 칸 청소
    if not clean[ny][nx] and board[ny][nx] != 1:
      y, x, direction = ny, nx, new_direction
      clean_floor(y, x, clean)
    # 네방향 모두 청소가 되어있거나 벽이라면 => 청소할곳이 없다면
    # 그리고 뒤칸이 벽이 아니라면
    # 방향유지한채로 뒤로 한칸 후진
    elif is_no_clean(y, x) and board[ry][rx] != 1:
      y, x = ry, rx
    # 청소할곳도 없고 뒤칸도 벽이라면
    # 작동을 멈춘다.
    elif is_no_clean(y, x) and board[ry][rx] == 1:
      return clean_score
    # 네방향중에 청소할곳이 한곳이라도 있긴 하지만
    # 현재 방향 기준으로 왼쪽이 아닐때는
    # 일단 좌회전을 한다
    else:
      direction=new_direction


print(sol())

