from sys import stdin
from queue import PriorityQueue

n, m = map(int, stdin.readline().split())


def ans():
  global n, m
  # pq = PriorityQueue()
  cost_list=list()
  for i in range(n):
    pi, li = map(int, stdin.readline().split())
    mile = list(map(int, stdin.readline().split()))

    # 신청하는 사람들이 정원보다 작으면
    # 1만 넣어도 신청가능
    if pi < li:
      cost_list.append(1)
      continue

    mile.sort()

    # 신청하는 사람들이 정원보다 같거나 많으면
    if pi >= li:
      cost_list.append(mile[pi - li])

  course = 0
  cost_list.sort()
  
  for cost in cost_list:
    if m>=cost:
      m-=cost
      course+=1
    else :
      break

  return course


print(ans())
