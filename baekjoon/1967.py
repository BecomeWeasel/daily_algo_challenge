from sys import stdin
from collections import deque

n = int(stdin.readline())
max_dist = -1


class node:
    def __init__(self):
        self.parent = 0
        self.parent_dist = 0
        self.childs = list()


def bfs(origin):
    global nodes, max_dist
    q = deque()
    q.append((origin, 0))

    check = [False for _ in range(n + 1)]
    check[origin] = True

    while q:
        current, dist = q.popleft()

        max_dist = max(max_dist, dist)

        # current 노드의 자식 노드를 방문하지 않았다면
        for childs_info in nodes[current].childs:
            if not check[childs_info[0]]:
                q.append((childs_info[0], dist + childs_info[1]))
                check[childs_info[0]] = True

        # current 노드가 루트가 아니고
        # current 노드의 부모를 방문하지 않았다면
        if nodes[current].parent != -1 and not check[nodes[current].parent]:
            q.append((nodes[current].parent, dist + nodes[current].parent_dist))
            check[nodes[current].parent] = True


nodes = [node() for _ in range(n + 1)]

# 1번 노드가 무조건 루트노드

nodes[1].parent = -1

for _ in range(n - 1):
    parent, child, dist = map(int, stdin.readline().split())
    nodes[parent].childs.append((child, dist))
    nodes[child].parent = parent
    nodes[child].parent_dist = dist

for i in range(1, n + 1):
    bfs(i)

print(max_dist)
