from sys import stdin, setrecursionlimit
import heapq as hq

setrecursionlimit(10**6)


N, M, A, B, C = map(int, stdin.readline().split())

edges = [list() for _ in range(N + 1)]

left, right = 987654321, -1

for _ in range(M):
    a, b, c = map(int, stdin.readline().split())

    edges[a].append((b, c))
    edges[b].append((a, c))

    left = min(left, c)
    right = max(right, c)

answer = 987654321

visit = [False for _ in range(N + 1)]

flag = False


def can_reach(upper_bound):
    p_q = [(0, A)]
    dist = [int(1e14) + 1 for _ in range(N + 1)]
    dist[A] = 0

    while p_q:
        total, node = hq.heappop(p_q)

        if dist[node] != total:
            continue

        for adj, cost in edges[node]:
            if cost > upper_bound:
                continue

            if dist[adj] > dist[node] + cost:
                dist[adj] = dist[node] + cost

                hq.heappush(p_q, (dist[adj], adj))

    return True if dist[B] <= C else False

    # global visit,flag

    # def dfs(node,upper_bound,total):
    #     global visit,flag

    #     if flag:
    #         return

    #     # print(node,upper_bound,total)

    #     if node==B:
    #         flag=True
    #         return

    #     for adj,cost in edges[node]:
    #         if not visit[adj] and  cost<=upper_bound and total+cost<=C and not flag:
    #             visit[adj] = True
    #             dfs(adj,upper_bound,total+cost)
    #             visit[adj] = False
    # visit[A]=True
    # dfs(A,upper_bound,0)
    # visit[A]=False

    # return flag


# print("======")

while left <= right:
    visit = [False for _ in range(N + 1)]
    mid = (left + right) // 2

    if can_reach(mid):
        # print(f"{mid} OK")
        answer = min(answer, mid)
        right = mid - 1
        flag = False
    else:
        left = mid + 1
    # print("======")

print(answer if answer != 987654321 else -1)
