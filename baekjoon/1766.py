from sys import stdin
from collections import defaultdict
import heapq

N, M = map(int, stdin.readline().split())


class p:
    def __init__(self, val) -> None:
        self.val = val
        self.indegree = 0

    def __lt__(self, other) -> bool:
        if self.indegree < other.indegree:
            return True
        elif self.indegree == other.indegree:
            return self.val < other.val
        else:
            return False

    def __str__(self) -> str:
        return "val : " + str(self.val) + " ind : " + str(self.indegree)


def sol():
    global p

    adjacency_list = defaultdict(list)
    problems_set = defaultdict()

    # problems[0]=(float('inf'),0)

    for i in range(N):
        problems_set[i + 1] = p(i + 1)

    for _ in range(M):
        src, dest = map(int, stdin.readline().split())
        adjacency_list[src].append(problems_set[dest])
        problems_set[dest].indegree += 1
    problems = [problems_set[i + 1] for i in range(N)]

    hq = []

    for p in problems:
        if p.indegree == 0:
            hq.append(p)

    heapq.heapify(hq)
    result = []
    for _ in range(N):
        p = heapq.heappop(hq)

        for adj in adjacency_list[p.val]:
            adj.indegree -= 1
            if adj.indegree == 0:
                heapq.heappush(hq, adj)
        result.append(p.val)

    return " ".join(map(str, result))


print(sol())
