from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M, T = map(int, stdin.readline().split())
grid = [[0] * (M + 1) for _ in range(N + 1)]
# 검을 줍기 전 경로와 줍고 난 후에 경로는 
# 서로 다른 탐색이니 check 배열을 3차원 배열로 구성
# BFS의 check 배열은 서로 다른 상황이 몇가지가 일어나느냐에 따라서
# 몇차원인지 결정되니
# 검을 얻었는가,y좌표,x좌표 3차원으로 구성
check = [[[False] * (M + 1) for _ in range(N + 1)] for _ in range (2)]

for i in range(1, N + 1):
  input_list = list(stdin.readline().split())
  for j in range(len(input_list)):
    grid[i][j + 1] = int(input_list[j])


def ans():
  return bfs()


def bfs():
  q = deque()
  # y,x,time,sword
  q.append((1, 1, 0, False))
  check[0][1][1] = True

  while q:
    y, x, time, sword = q.popleft()

    if y == N and x == M and time <= T:
      return time

    if time >= T:
      continue

    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]

      if ny > N or nx > M or ny < 1 or nx < 1:
        continue

      if sword:
        # (nx,ny)는 중요하지 않음
        # 칼이 있으면 다 무시하고 지나갈수 잇음
        if not check[1][ny][nx]:
          q.append((ny, nx, time + 1, sword))
          check[1][ny][nx] = True
      else:
        if grid[ny][nx] != 1 and not check[0][ny][nx]:
          # (nx,ny)에 칼이 있을때
          if grid[ny][nx] == 2:
            q.append((ny, nx, time + 1, True))
            check[0][ny][nx] = True
          else:
            q.append((ny, nx, time + 1, False))
            check[0][ny][nx] = True
  return "Fail"


print(ans())
