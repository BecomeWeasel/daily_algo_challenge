from collections import defaultdict
import heapq as hq


def solution(n, s, a, b, fares):
    answer = 0

    edges = defaultdict(list)

    for c, d, f in fares:
        edges[c].append((d, f))
        edges[d].append((c, f))

    distances = defaultdict(dict)

    for i in range(1, n + 1):
        distances[i] = {node: float("inf") for node in range(1, n + 1)}
        distances[i][i] = 0

    for i in range(1, n + 1):
        q = list()

        hq.heappush(q, (distances[i][i], i))

        while q:
            cur_dist, node = hq.heappop(q)

            if distances[i][node] < cur_dist:
                continue

            for adjacent_node, dist in edges[node]:
                w = cur_dist + dist

                if w < distances[i][adjacent_node]:
                    distances[i][adjacent_node] = w

                    hq.heappush(q, (w, adjacent_node))
    answer = float("inf")

    for i in range(1, n + 1):
        answer = min(answer, distances[s][i] + distances[i][a] + distances[i][b])

    return answer
