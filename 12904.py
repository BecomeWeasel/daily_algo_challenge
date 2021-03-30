from sys import stdin
from collections import deque

S = list(stdin.readline().rstrip('\n'))
T = list(stdin.readline().rstrip('\n'))


def sol():
  global S, T
  # BFS 풀이 메모리초과
  # result_string = S

  # q = deque()
  # check = set()
  # check.add(result_string)
  # q.append((result_string, result_string.count('A'), result_string.count('B')))

  # while len(q) != 0:
  #   string, count_a, count_b = q.popleft()

  #   if count_a + 1 <= num_A and count_b <= num_B and string + 'A' not in check:

  #     if len(string)+1 == len(T) and not string+'A' == T:
  #       continue

  #     if (string + 'A') == T:
  #       return 1

  #     q.append((string + 'A', count_a + 1, count_b))
  #     check.add(string + 'A')

  #   if count_a <= num_A and count_b + 1 <= num_B and string[::
  #                                                           -1] + 'B' not in check:
  #     if len(string)+1 == len(T) and not string[::-1]+'B' == T:
  #       continue

  #     if (string[::-1] + 'B') == T:
  #       return 1
  #     q.append((string[::-1] + 'B', count_a, count_b + 1))
  #     check.add(string[::-1] + 'B')

  # return 0

  # 생각을 바꿔서 T에서 한단계씩 이전으로 되돌아가는것임
  # T의 마지막이 A라면 이전은 무조건 T[:len(T)-1]이고
  # T의 마지막이 B라면 이전은 T.pop() 후에 T[::-1]임
  # 이렇게 이전으로 계속 되돌아갔을때 S와 T가 일치하는지만 보면됨

  # ctrl-z를 해서 S로 되돌아갈수 잇느냐를 판단
  while len(S) != len(T):
    # T의 마지막이 A라면 
    if T[-1] == 'A':
      T=T[:len(T)-1]
    # T의 마지막이 B라면
    else:
      T.pop()
      T = T[::-1]

  if S == T:
    return 1
  else:
    return 0


print(sol())