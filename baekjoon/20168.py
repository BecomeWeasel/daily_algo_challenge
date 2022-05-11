from sys import stdin

answer = 987654321

N, M, A, B, C = map(int, stdin.readline().split())


def dfs(node, current_cost, current_top, visited, edges):
    global answer, B, C
    if node == B:
        answer = min(current_top, answer)
        return

    for adj, cost in edges[node]:
        if visited[adj]:
            continue

        if cost + current_cost <= C:
            visited[adj] = True
            dfs(adj, cost + current_cost, max(current_top, cost), visited, edges)
            visited[adj] = False


def sol():
    global answer

    edges = [list() for _ in range(N + 1)]

    for _ in range(M):
        src, dest, cost = map(int, stdin.readline().split())

        edges[src].append((dest, cost))
        edges[dest].append((src, cost))

    visited = [False for _ in range(N + 1)]

    visited[A] = True

    dfs(node=A, current_cost=0, current_top=0, visited=visited, edges=edges)

    return answer if answer != 987654321 else -1


print(sol())
