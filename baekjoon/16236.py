from sys import stdin
from collections import deque
from queue import PriorityQueue

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# class fish:
#   def __init__(self, y, x, dist, size):
#     self.y = y
#     self.x = x
#     self.dist = dist
#     self.size = size


N = int(stdin.readline())
grid = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
  input_list = list(map(int, stdin.readline().split()))
  for j in range(len(input_list)):
    grid[i][j + 1] = int(input_list[j])

shark_y, shark_x = 1, 1
time = 0
shark_size = 2
current_eat = 0
# 먹을만한 물고기들의 예비모임
# 거리,y가 가장 적은것,x가 가장 적은 것 순서대로
# 정렬되어야 하니 우선순위 큐
fish_pool = PriorityQueue()

# 시작점 찾기
for i in range(1, N + 1):
  for j in range(1, N + 1):
    if grid[i][j] == 9:
      shark_y = i
      shark_x = j


def ans():
  global time, shark_size, current_eat, fish_pool, shark_x, shark_y
  while True:
    # 물고기 예비모임 비우기
    while not fish_pool.empty():
      fish_pool.get()

    bfs()

    # 잡아 먹을수 있는 물고기가 아무도 없다면
    if fish_pool.qsize() == 0:
      print(time)
      return

    # 1순위 물고기 잡아먹은후
    # 상어 위치 변경

    grid[shark_y][shark_x] = 0

    # 가장 가깝고
    # 가까운 것들중에서 가장 위쪽에
    # 가깝고 가장 위쪽인것들 중 가장 왼쪽
    dist, y, x = fish_pool.get()

    current_eat += 1
    # 상어의 크기만큼 물고기를 먹었으면
    # 진급해야함
    if current_eat >= shark_size:
      shark_size += 1
      current_eat = 0

    shark_y = y
    shark_x = x
    time += dist

    # 상어가 물고기를 먹고 이동
    grid[shark_y][shark_x] = 9


def bfs():
  global shark_x, shark_y, fish_pool
  check = [[False] * (N + 1) for _ in range(N + 1)]
  q = deque()
  q.append((shark_y, shark_x, 0))
  check[shark_y][shark_x] = True
  while q:
    y, x, dist = q.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]

      if ny > N or nx > N or ny < 1 or nx < 1:
        continue

      # 물고기를 탐색
      # 빈 공간(0)이거나 나보다 사이즈가 작거나 같으면
      # 그 공간으로 움직일수 있음
      if not check[ny][nx] and grid[ny][nx] <= shark_size:

        # 뚫려있는 빈 공간이 아니고 상어 크기보다 작은 물고기면
        if grid[ny][nx] != 0 and grid[ny][nx] < shark_size:
          fish_pool.put((dist + 1, ny, nx))
          check[ny][nx]=True
        else :
          check[ny][nx] = True
          q.append((ny, nx, dist + 1))


ans()