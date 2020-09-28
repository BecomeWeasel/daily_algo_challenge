from sys import stdin
from collections import deque

n, T = map(int, stdin.readline().split())
check = set()
hole = set()
for _ in range(n):
  x, y = map(int, stdin.readline().split())
  hole.add((y, x))


def ans():
  return bfs()


def bfs():
  global check
  q = deque()
  q.append((0, 0, 0))

  # check 배열의 인자 4개는
  # 출발점 y,x 와 도착점 y,x
  # 이렇게 나눈 이유는 한 칸만큼 움직여서 도착한 (a,b)와
  # 두 칸만큼 움직여서 도착한 (a,b)는 다른 것임
  check.add((0, 0, 0, 0))

  while q:
    y, x, time = q.popleft()

    for diff_y in range(-2, 3, 1):
      for diff_x in range(-2, 3, 1):
        ny = y + diff_y
        nx = x + diff_x

        if ny > 200000 or ny < 0 or nx > 1000000 or nx < 0:
          continue

        if (ny, nx) in hole and not (y, x, ny, nx) in check:
          if ny == T:
            return time + 1
          else:
            q.append((ny, nx, time + 1))
            check.add((y, x, ny, nx))

  return -1


print(ans())