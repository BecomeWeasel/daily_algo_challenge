from sys import stdin, stdout, setrecursionlimit
from collections import deque


setrecursionlimit(10**5)
T = int(stdin.readline())


def sol():
    N, K = map(int, stdin.readline().split())

    cost = list(map(int, stdin.readline().split()))

    connection = [[False for _ in range(N + 1)] for _ in range(N + 1)]
    time = [-1 for _ in range(N + 1)]

    for _ in range(K):
        ori, dest = map(int, stdin.readline().split())

        connection[ori][dest] = True

    W = int(stdin.readline())

    return dp(cost, connection, time, W, N)


def dp(cost, connection, time, target, N):

    if time[target] != -1:
        return time[target]

    req = []

    for i in range(1, N + 1):
        if target == i:
            continue
        # target을 건설하는데 i가 필수적이라면
        if connection[i][target] == True:
            req.append(i)

    req_time = [dp(cost, connection, time, x, N) for x in req]

    time[target] = cost[target - 1] + max(req_time) if len(req_time) != 0 else cost[target - 1]

    return time[target]


for _ in range(T):
    print(sol())
