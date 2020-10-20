from sys import stdin
from collections import deque


def print_route(route):
  print(route.replace(",", " "))
  return 0


def ans():
  q = deque()
  q.append((N, 0, str(N)))
  check = [False for _ in range(100001)]
  check[N] = True

  while q:
    pos, time, route = q.popleft()

    if pos == K:
      print(time)
      print_route(route)

    for npos in pos - 1, pos + 1, pos * 2:
      if npos > 100000 or npos < 0:
        continue

      if not check[npos]:
        q.append((npos, time + 1, route + "," + str(npos)))
        check[npos] = True


N, K = map(int, stdin.readline().split())
ans()
