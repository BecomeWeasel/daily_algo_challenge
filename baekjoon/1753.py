from sys import stdin
from collections import defaultdict
import heapq as hq


def sol():
    V, E = map(int, stdin.readline().split())

    src = int(stdin.readline())

    distances = {node: float('inf') for node in range(1, V + 1)}

    distances[src] = 0

    q = list()

    edges = defaultdict(list)

    for _ in range(E):
        u, v, w = map(int, stdin.readline().split())
        edges[u].append((v, w))

    hq.heappush(q, (distances[src], src))

    while q:
        cur_dist, node = hq.heappop(q)

        if distances[node] < cur_dist:
            continue

        for adjacent_node, dist in edges[node]:
            w = cur_dist + dist

            if w < distances[adjacent_node]:
                distances[adjacent_node] = w

                hq.heappush(q, (w, adjacent_node))

    for i in range(1, V + 1):
        if distances[i] == float('inf'):
            print("INF")
        else:
            print(distances[i])


sol()
