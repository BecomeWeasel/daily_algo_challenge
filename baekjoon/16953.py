import sys
from collections import deque


def ans(A, B):
    # result=bfs()

    cnt = 0
    while True:
        if A > B:
            return -1
        if A == B:
            return cnt + 1

        if B % 10 == 1:
            B = int(B / 10)
        elif B % 2 == 0:
            B = int(B / 2)
        else:
            return -1
        cnt += 1

    return cnt + 1

    # return result


def bfs():
    q = deque()
    q.append((A, 0))
    while q:
        num, cnt = q.popleft()

        for newnum in num * 2, int(str(num) + "1"):
            if newnum > B:
                continue
            if newnum == B:
                return cnt + 2
            q.append((newnum, cnt + 1))

    return -1


A, B = map(int, sys.stdin.readline().split())

# B의 범위가 10^9이기 때문에 visited 배열 초과
# visited 배열 없어도 풀 수 있어서 제외
# visited=[False for _ in range(B+1)]
# visited[A]=True

print(ans(A, B))
