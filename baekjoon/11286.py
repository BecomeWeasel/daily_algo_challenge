from sys import stdin
import heapq

N = int(stdin.readline())


class compare_node():
  def __init__(self, value):
    self.abs_value = abs(value)
    self.value = value

  def __lt__(self, other):
    # 일단 절댓값이 작은것이 앞으로 오게
    if self.abs_value < other.abs_value:
      return True
    # 절댓값이 같다면 원래 값이 작은것이 앞으로 오게
    elif self.abs_value == other.abs_value:
      return self.value < other.value
    else:
      return False


def sol():

  l = list()

  for _ in range(N):

    op = int(stdin.readline())

    if op == 0:
      if len(l) == 0:
        print(0)
      else:
        print(l[0].value)
        heapq.heappop(l)
    else:
      heapq.heappush(l, compare_node(op))


sol()
