from sys import stdin
from collections import deque
from queue import PriorityQueue


def ans():
  bfs()
  result_list.sort()
  min_value = result_list[0]

  cnt = 0

  for value in result_list:
    if value == min_value:
      cnt += 1

  print(min_value)
  print(cnt)


def bfs():
  q = deque()
  q.append((N, 0))
  visited[N] = 0

  while q:
    pos, cnt = q.popleft()

    if pos == K:
      result_list.append(cnt)
      continue

    select = [pos - 1, pos + 1, pos * 2]
    for j in range(3):
      npos = select[j]

      if npos < 0 or npos > 100000: continue

      # npos를 탐색하지 않았거나(-1)
      # 이전에 방문한 시간과 같은 시간에 도착했거나
      # e.g.) 1+1 = 2 1*1=2
      if visited[npos] == -1 or visited[npos] == cnt:
        if npos == K:
          result_list.append(cnt + 1)
        else:
          q.append((npos, cnt + 1))
          visited[npos] = cnt


N, K = map(int, stdin.readline().split())

# visited[i] : i번째에 방문한 시간
# -1이라면 방문하지 않았음
visited = [-1 for _ in range(100001)]

result_list = []
ans()
