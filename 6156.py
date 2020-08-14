from sys import stdin
from collections import deque


# node에 자기보다 약한것
# 자기보다 강한것의 노드를 넣고
# BFS 탐색을 시도
# 만약 자기보다 강한 노드와 약한 노드 개수가 합쳐서 N-1개라면
# 자신의 등수는 정해짐
class node:
  def __init__(self):
    self.weaker = []
    self.stronger = []


def ans():
  cnt = 0

  for i in range(1, N + 1):
    node_cnt = 0
    visited = [False for _ in range(N + 1)]
    visited[i] = True
    node_cnt += weak_bfs(i, visited)
    visited = [False for _ in range(N + 1)]
    visited[i] = True
    node_cnt += strong_bfs(i, visited)

    # 자기보다 약하거나 강한사람이 합쳐서
    # N-1명이라면 자기순위는 정해짐
    if node_cnt == N - 1:
      cnt += 1

  return cnt


# origin보다 약한 쪽만 탐색
def weak_bfs(origin, visited):
  cnt = 0
  q = deque()
  q.append((origin))

  while q:
    src = q.popleft()
    for weak_node in node_set[src].weaker:
      if not visited[weak_node]:
        visited[weak_node] = True
        cnt += 1
        q.append((weak_node))

  return cnt


# origin보다 약한 쪽만 탐색
def strong_bfs(origin, visited):
  cnt = 0
  q = deque()
  q.append((origin))

  while q:
    src = q.popleft()
    for strong_node in node_set[src].stronger:
      if not visited[strong_node]:
        visited[strong_node] = True
        cnt += 1
        q.append((strong_node))

  return cnt


N, M = map(int, stdin.readline().split())
node_set = [node() for _ in range(N + 1)]

for i in range(M):
  win, lose = map(int, stdin.readline().split())

  
  node_set[win].weaker.append(lose)
  node_set[lose].stronger.append(win)

print(ans())
