from sys import stdin
from collections import deque


def ans():
  while q:
    y1, x1, y2, x2 = q.popleft()

    total_sum = 0
    for i in range(y1, y2 + 1):
      total_sum += sum_grid[i][x2] - sum_grid[i][x1 - 1]
    print(total_sum)


N, M = map(int, stdin.readline().split())
grid = [[0] * (N + 1) for _ in range(N + 1)]
sum_grid = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
  tmp = list(map(int, stdin.readline().split()))
  tmp_sum = 0
  for j in range(1, N + 1):
    tmp_sum += tmp[j - 1]
    sum_grid[i][j] = tmp_sum

q = deque()
# print('\n')
# print(sum_grid)

for k in range(M):
  tmp_y1, tmp_x1, tmp_y2, tmp_x2 = map(int, stdin.readline().split())
  q.append((tmp_y1, tmp_x1, tmp_y2, tmp_x2))

ans()
