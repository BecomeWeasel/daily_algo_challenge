from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
visited = [False for _ in range(N + 1)]
result = []


def dfs(v, adjacency):
    global visited

    for node in adjacency[v]:
        if not visited[node]:
            visited[node] = True
            dfs(node, adjacency)
    result.append(v)


def sol():
    global result, visited

    adjacency = [list() for _ in range(N + 1)]

    # adjacency matrix로 하니까 메모리초과
    # adjacency list로 구현
    for _ in range(M):
        a, b = map(int, stdin.readline().split())
        adjacency[a].append(b)

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            dfs(i, adjacency)

    # dfs 수행 결과 반대로 출력
    result.reverse()
    print(" ".join(map(str, result)))


sol()
