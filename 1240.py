from sys import stdin
from collections import deque

def bfs(src, dest):
  global node_dist

  check = [False for _ in range(N + 1)]
  check[src] = True
  q = deque()
  q.append((src, 0))

  while q:
    pos, dist_sum = q.popleft()

    for npos in connecion_list[pos]:
      if not check[npos]:
        q.append((npos, dist_sum + node_dist[pos][npos]))
        check[npos] = True

      if npos == dest:
        return dist_sum + node_dist[pos][npos]


N, M = map(int, stdin.readline().split())

# node_dist[i][j] : i 와 j 사이의 거리
# node_dist[i][j]가 -1이면 연결되어 있지 않다는 뜻
node_dist = [[-1] * (N + 1) for _ in range(N + 1)]
connecion_list = [list() for _ in range(N + 1)]

for _ in range(N - 1):
  src, dest, d_value = map(int, stdin.readline().split())
  node_dist[src][dest] = node_dist[dest][src] = d_value
  connecion_list[src].append(dest)
  connecion_list[dest].append(src)

for _ in range(M):
  src, dest = map(int, stdin.readline().split())
  print(bfs(src, dest))


