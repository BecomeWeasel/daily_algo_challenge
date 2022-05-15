from sys import stdin
from math import sqrt

N, M = map(int, stdin.readline().split())

parent = [i for i in range(N + 1)]


def find_parent(x):
    global parent
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def sol():
    # 엣지 추가하냐 마냐는 중요한게 아니라,
    # 이미 모든 엣지가 있다 생각하고
    # 모든 노드를 연결하는 최소 비용 엣지들의 집합에서 미리 설치되어 있는것들만 빼주면 됨.
    # MST 문제

    # 아니면 원래 있던 엣지는 비용 0으로 하면됨

    # 크루스칼 쓸거고
    # 엣지 개수는 E=N^2개
    # O(ElogE)=O(N^2*logN)=O(1000^2*log1000)

    nodes = [0 for _ in range(N + 1)]
    edges = []
    answer = 0

    for i in range(1, N + 1):
        x, y = map(int, stdin.readline().split())
        nodes[i] = (y, x)

    for _ in range(M):
        src, dest = map(int, stdin.readline().split())

        edges.append((src, dest, 0))

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            y1, x1 = nodes[i]
            y2, x2 = nodes[j]

            edges.append((i, j, sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)))

    edges.sort(key=lambda x: x[2])

    for u, v, cost in edges:
        if find_parent(u) != find_parent(v):
            union_parent(u, v)
            answer += cost

    return "{:.2f}".format(answer)


print(sol())
