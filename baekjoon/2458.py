from sys import stdin
from collections import deque


class person:
    def __init__(self):
        self.greater = set()
        self.less = set()


N, M = map(int, stdin.readline().split())
persons = [person() for _ in range(N + 1)]
rank = [0 for _ in range(N + 1)]


for _ in range(M):
    a, b = map(int, stdin.readline().split())
    persons[a].greater.add(b)
    persons[b].less.add(a)


def ans():
    for i in range(1, N + 1):
        bfs(i, 0)
        bfs(i, 1)

    count = 0
    for t in rank:
        if t == N - 1:
            count += 1
    # print(rank)
    return count


# direction : 0 이면 작은 쪽 검사, 1이면 큰 쪽 검사
def bfs(origin, greater_direction):
    global persons, rank
    count = 0
    check = [False for _ in range(N + 1)]
    check[origin] = True
    q = deque()
    q.append(origin)

    while q:
        pos = q.popleft()

        if greater_direction:
            for t in persons[pos].greater:
                if not check[t]:
                    q.append(t)
                    check[t] = True
                    count += 1
        else:
            for t in persons[pos].less:
                if not check[t]:
                    q.append(t)
                    check[t] = True
                    count += 1

    rank[origin] += count


print(ans())
