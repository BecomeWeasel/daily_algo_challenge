from sys import stdin
from collections import deque


def ans():
    print(bfs())


def bfs():
    q = deque()
    if S == T:
        return 0
    q.append((S, ""))
    visit.add(S)

    while q:
        s, op_list = q.popleft()

        if s == T:
            return op_list

        if s * s <= 10e9 and s * s not in visit:
            q.append((s * s, op_list + "*"))
            visit.add(s * s)

        if s + s <= 10e9 and s + s not in visit:
            q.append((s + s, op_list + "+"))
            visit.add(s + s)

        # 의미없음
        # if 0 not in visit:
        #   q.append((s - s, op_list + '-'))
        #   visit.add(0)

        if s != 0 and 1 not in visit:
            q.append((1, op_list + "/"))
            visit.add(1)

    return -1


S, T = map(int, stdin.readline().split())
# 탐색해야하는 노드의 개수가 매우 많으므로(10^9개)
# 배열이 아니라 set으로 관리
visit = set()
ans()
