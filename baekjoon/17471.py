from sys import stdin
from sys import maxsize
from collections import deque

N = int(stdin.readline())
connection = [[False] * (N + 1) for _ in range(N + 1)]
people = [-1]
people = people + list(map(int, stdin.readline().split()))
MIN = maxsize

for i in range(1, N + 1):
  input_list = list(map(int, stdin.readline().split()))
  for k in range(input_list[0]):
    connection[i][input_list[k + 1]] = connection[input_list[k + 1]][i] = True


def bfs(group):
  q = deque()
  local_check = [False for _ in range(N + 1)]

  q.append((group[0]))
  local_check[group[0]] = True
  cnt, peoples = 1, 0

  while q:
    target = q.popleft()
    peoples += people[target]

    for i in range(1, N + 1):
      # i번 구역이 target번과 인접해있고
      # i번이 group 내부에 선정되어 있고
      # 아직 방문하지 않았다면
      if connection[target][i] and i in group and not local_check[i]:
        local_check[i] = True
        cnt += 1
        q.append((i))

  # bfs 안에서 탐색이 group 내부의 
  # 구역 개수만큼 수행되지 않았다면
  # 한 곳은 연결되어 있지 않았으므로
  # 선거구를 잘못 선정한것
  if cnt == len(group):
    return peoples
  else:
    return 0


def dfs(count, target_count, start, c):
  global MIN
  if count == target_count:
    # 1선거구와 2선거구로 나눠서 넣음
    group1, group2 = list(), list()

    for i in range(1, N + 1):
      if c[i]:
        group1.append(i)
      else:
        group2.append(i)

    # 1선거구나 2선거구에 대해서
    # bfs를 수행한 값이 하나라도 0이라면
    # 선거구가 똑바로 연결되어 있지 않다는 것이므로
    # 빠져나감
    ans1 = bfs(group1)
    if ans1 == 0:
      return
    ans2 = bfs(group2)
    if ans2 == 0:
      return

    
    MIN = min(MIN, abs(ans1 - ans2))
    return
  
  for i in range(start,N+1):
    if c[i]:
      continue
    c[i]=True
    dfs(count+1,target_count,i,c)
    c[i]=False



def ans():
  # 먼저 두 선거구로 나누기 위해 dfs를 사용해서
  # 분리
  for i in range(1, N):
    c = [False for _ in range(N + 1)]
    dfs(0,i,1,c)

  return MIN==maxsize and -1 or MIN

print(ans())
