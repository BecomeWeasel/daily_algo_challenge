from re import M
from sys import stdin
import heapq as hq
from collections import defaultdict

N, M = map(int, stdin.readline().split())

edges = [defaultdict(int) for _ in range(N + 1)]

# 2307번과 동일

for _ in range(M):
    a, b, t = map(int, stdin.readline().split())

    edges[a][b] = t
    edges[b][a] = t
dist = [1e10 for _ in range(N + 1)]

prev = [-1 for _ in range(N + 1)]

pq = []

pq.append((0, 1))

dist[1] = 0

while pq:
    current_dist, current_node = hq.heappop(pq)

    if dist[current_node] < current_dist:
        continue

    for new_node, new_dist in edges[current_node].items():
        distance = current_dist + new_dist

        if distance < dist[new_node]:
            dist[new_node] = distance
            prev[new_node] = current_node
            hq.heappush(pq, (distance, new_node))

origin_min_distance = dist[N]

s_path = []
dest = N
while dest != -1:
    s_path.append((dest, prev[dest]))
    dest = prev[dest]

s_path.pop()

answer = -1

for src, dest in s_path:
    origin_value = edges[src][dest]

    edges[src][dest] = edges[dest][src] = 1e10

    dist = [1e10 for _ in range(N + 1)]

    pq = []

    pq.append((0, 1))

    dist[1] = 0

    while pq:
        current_dist, current_node = hq.heappop(pq)

        if dist[current_node] < current_dist:
            continue

        for new_node, new_dist in edges[current_node].items():
            distance = current_dist + new_dist

            if distance < dist[new_node]:
                dist[new_node] = distance
                prev[new_node] = current_node
                hq.heappush(pq, (distance, new_node))

    answer = max(answer, dist[N])

    edges[src][dest] = edges[dest][src] = origin_value


print(answer)
