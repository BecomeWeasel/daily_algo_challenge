from sys import stdin


T = int(stdin.readline())


def sol(N):
    visit = [False for _ in range(N + 1)]

    parent = [-1 for _ in range(N + 1)]

    for _ in range(N - 1):
        A, B = map(int, stdin.readline().split())

        parent[B] = A

    a, b = map(int, stdin.readline().split())

    p, curr = parent[a], a
    visit[a] = True
    i = 0
    while curr != -1:
        # print(curr,p)
        visit[curr] = True
        p, curr = parent[p], parent[curr]

    p, curr = parent[b], b

    while not visit[curr]:
        p, curr = parent[p], parent[curr]

    return curr


for _ in range(T):
    N = int(stdin.readline())

    print(sol(N))
