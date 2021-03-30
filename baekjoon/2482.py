from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split())
q = deque()

for i in range(1, N + 1):
  q.append(i)


def ans():
  global q
  print_q=deque()

  while q:
    for t in range(K):
      tmp = q.popleft()
      if t != K-1:
        q.append(tmp)
      else :
        print_q.append(tmp)
        

  s = "<"
  while print_q:
    num = print_q.popleft()
    if not print_q:
      s = s + str(num) + ">"
    else:
      s = s + str(num) + ", "
  print(s)


ans()
