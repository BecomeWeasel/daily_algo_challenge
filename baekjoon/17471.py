from sys import stdin
from itertools import combinations
from collections import deque

N = int(stdin.readline())


def sol():
  # 각 구역마다 인구수
  people = list(map(int, stdin.readline().split()))

  connection = [[False for _ in range(N)] for _ in range(N)]

  for i in range(N):
    temp = list(map(int, stdin.readline().split()))

    # 구역들끼리 연결되어있는 정보를 기록
    if not temp[0] == 0:
      for connected_node in temp[1:]:
        connection[i][connected_node-1] = connection[connected_node-1][i] = True

  MIN_DIFF = 1e9

  district_list = [i for i in range( N )]

  # 딱 절반까지만 하면 됨
  for i in range(1, int(N / 2) + 1):
    
    # 조합을 이용함
    for g1 in list(combinations(district_list, i)):
      selected_district = [False for _ in range(N)]

      # 1선거구에 선정됨을 표시
      for district in g1:
        selected_district[district] = True

      # 1선거구 ,2선거구
      election_one, election_two = deque(),deque()

      for j, is_one in enumerate(selected_district):
        if is_one:
          election_one.append(j)
        else:
          election_two.append(j)

      diff = bfs(election_one, election_two,people,connection)

      MIN_DIFF = min(MIN_DIFF, diff) if diff != -1 else MIN_DIFF

  return -1 if MIN_DIFF == 1e9 else MIN_DIFF


def bfs(e1, e2,people,connection):
  check = [False for _ in range(N)]
  e1_count,e2_count=0,0
  
  
  front=e1.popleft()

  q=deque()
  q.append(front)
  check[front]=True

  while len(q)!=0:
    node=q.popleft()
    e1_count+=people[node]

    for another_node,is_connected in enumerate(connection[node]):
      # 이 구역에 연결되어있는 다른 구역에 아직 방문하지 않았고그 구역이
      # 같은 선거구 내일때
      if is_connected==True and another_node in e1 and not check[another_node]:
        check[another_node]=True
        q.append(another_node)
  
  front=e2.popleft()

  q=deque()
  q.append(front)
  check[front]=True

  while len(q)!=0:
    node=q.popleft()
    e2_count+=people[node]

    for another_node,is_connected in enumerate(connection[node]):
      # 이 구역에 연결되어있는 다른 구역에 아직 방문하지 않았고그 구역이
      # 같은 선거구 내일때
      if is_connected==True and another_node in e2 and not check[another_node]:
        check[another_node]=True
        q.append(another_node)
  
  # 방문하지 않은 구역이 있다는건 
  # 연결되지 않은 구역이 선거구내에 있다는것임
  for boolean in check:
    if not boolean:
      return -1
  return abs(e1_count-e2_count)

print(sol())