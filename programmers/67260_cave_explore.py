from collections import defaultdict
from sys import setrecursionlimit

setrecursionlimit(10**6)


def solution(n, path, order):
    answer = True

    count = 0

    indegree = defaultdict(int)

    edge = [list() for _ in range(n)]

    def dfs(node):
        nonlocal count, indegree, n, edge

        for neigbor in edge[node]:
            # print(f"current node is {node} and next is {neigbor}")
            indegree[neigbor] -= 1

            if indegree[neigbor] == 0:
                # print(f"{neigbor} step in ")
                count += 1
                dfs(neigbor)

    # for p in path:
    #     ori,dest=p[0],p[1]

    #     indegree[dest]+=1

    #     edge[ori].append(dest)

    graph = [list() for _ in range(n)]

    for p in path:
        ori, dest = p[0], p[1]

        graph[ori].append(dest)
        graph[dest].append(ori)

    unidirectional = [list() for _ in range(n)]

    visit = set()

    def simple_dfs(node, step):
        nonlocal graph

        for neighbor in graph[node]:
            if neighbor in visit:
                continue
            visit.add(neighbor)
            unidirectional[node].append(neighbor)
            simple_dfs(neighbor, step)

    visit.add(0)
    simple_dfs(0, 0)

    for node in range(n):
        edge_from_node = unidirectional[node]

        for e in edge_from_node:
            indegree[e] += 1
            edge[node].append(e)

    for o in order:
        ori, dest = o[0], o[1]

        indegree[dest] += 1

        edge[ori].append(dest)

    count = 1
    dfs(0)

    if count == n:
        return True
    else:
        return False