from sys import stdin
from collections import defaultdict
import heapq as hq


def sol():
    N, E = map(int, stdin.readline().split())

    edges = defaultdict(list)

    for _ in range(E):
        a, b, c = map(int, stdin.readline().split())
        edges[a].append((b, c))
        edges[b].append((a, c))

    v1, v2 = map(int, stdin.readline().split())

    # 두가지 경우
    # 1 -> v1 -> v2 -> N : route 1
    # 1 -> v2 -> v1 -> N : route 2

    r1, r2 = 0, 0

    distances = {node: float("inf") for node in range(1, N + 1)}

    distances[1] = 0

    q = [(distances[1], 1)]

    while q:
        cur_d, node = hq.heappop(q)

        if distances[node] < cur_d:
            continue

        for adjacent_node, d in edges[node]:
            w = d + cur_d

            if w < distances[adjacent_node]:
                distances[adjacent_node] = w

                hq.heappush(q, (w, adjacent_node))

    r1 += distances[v1]
    r2 += distances[v2]

    distances = {node: float("inf") for node in range(1, N + 1)}

    distances[v1] = 0

    q = [(distances[v1], v1)]

    while q:
        cur_d, node = hq.heappop(q)

        if distances[node] < cur_d:
            continue

        for adjacent_node, d in edges[node]:
            w = d + cur_d

            if w < distances[adjacent_node]:
                distances[adjacent_node] = w

                hq.heappush(q, (w, adjacent_node))

    r1 += distances[v2]
    r2 += distances[N]

    distances = {node: float("inf") for node in range(1, N + 1)}

    distances[v2] = 0

    q = [(distances[v2], v2)]

    while q:
        cur_d, node = hq.heappop(q)

        if distances[node] < cur_d:
            continue

        for adjacent_node, d in edges[node]:
            w = d + cur_d

            if w < distances[adjacent_node]:
                distances[adjacent_node] = w

                hq.heappush(q, (w, adjacent_node))

    r1 += distances[N]
    r2 += distances[v1]

    return min(r1, r2) if r1 != float("inf") and r2 != float("inf") else -1


print(sol())
