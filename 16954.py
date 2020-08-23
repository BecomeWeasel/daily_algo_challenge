from sys import stdin
from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dx = [0, -1, -1, -1, 0, 1, 1, 1, 0]
map_size = 8


def move():
  global map2
  # 맨 밑칸부터 움직여야지 겹쳐짐이 없음
  for i in range(map_size - 1, -1, -1):
    for j in range(map_size):
      if map2[i][j] == 1:
        if i == map_size - 1:
          map2[i][j] = 0
        else:
          map2[i][j] = 0
          map2[i + 1][j] = 1


def ans():
  return bfs()


def bfs():
  global map2, visit

  # queue를 두개로 구성하는 이유는
  # 첫번째 움직임 후에 벽이 움직여야 하니까
  # 이동해야 하는 지점을 따로 move_queue로 관리해주고
  # queue에 move_queue의 내용물을 전부 복사
  q = deque()
  move_q = deque()
  move_q.append((map_size - 1, 0, 0))
  visit.add((map_size - 1, 0, 0))

  while True:
    while move_q:
      tmpy, tmpx, tmptime = move_q.popleft()
      q.append((tmpy, tmpx, tmptime))
    while q:
      y, x, time = q.popleft()
      
      # 목표점에 도착했으면
      if y == 0 and x == map_size - 1:
        return 1

      if map2[y][x] == 1:
        continue

      for k in range(9):
        ny = y + dy[k]
        nx = x + dx[k]

        if ny < 0 or nx < 0 or nx > map_size - 1 or ny > map_size - 1:
          continue
        
        # 1초 뒤에 한번도 안움직이는 경우가 있기 때문에
        # 시간도 체크해줘야함
        if not (ny, nx, time + 1) in visit and map2[ny][nx] == 0:
          move_q.append((ny, nx, time + 1))
          visit.add((ny, nx, time + 1))

    # 아예 움직일 곳이 없으면 탐색불가
    if not move_q and not q:
      return 0
    # 벽을 움직임
    move()
  return 0


grid_map = [[' '] for _ in range(map_size)]

for i in range(map_size):
  s = stdin.readline()
  s = s[0:map_size]
  grid_map[i] = s

# visit = [[False] * map_size for _ in range(map_size)]
# 1초 뒤에 한번도 안 움직이는 경우가 있으니
# 3차원 배열로 구현해야하는데
# 시간이 정해져 있지 않기 때문에 set으로 visit 관리
visit = set()
map2 = [[0] * map_size for _ in range(map_size)]
for i in range(map_size):
  for j in range(map_size):
    if grid_map[i][j] == '.':
      map2[i][j] = 0
    else:
      map2[i][j] = 1
print(ans())
