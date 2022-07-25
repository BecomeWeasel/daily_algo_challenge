from sys import stdin, setrecursionlimit

N, K = map(int, stdin.readline().split())


def sol():
    cows = [-1]
    edges = [list() for _ in range(N + 1)]
    for _ in range(N - 1):
        src, dest = map(int, stdin.readline().split())

        edges[src].append(dest)
        edges[dest].append(src)

    for _ in range(N):
        cows.append(int(stdin.readline()))

    # 소의 개수가 0부터 시작임
    # 여기서 문제가 생김.
    # d[current][k]이 0이 아니면, 계산이 되었다고 판단하는데,
    # d[current][0]이 0인 경우가 있음 ..
    # 그러니까 k가 음수로 빠져버림
    # d=[[0 for _ in range(K+1)] for _ in range(N+1)]
    d = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]

    def dp(current, k):

        nonlocal d, cows

        # print(current,k)
        # 이미 계산되었다면,

        if d[current][k] != -1:
            return d[current][k]

        d[current][k] = d[current][k - 2]

        for adj in edges[current]:
            # 이 부분에서 중복을 빼주는건데 여기서 문제가 생김
            #
            # a=dp(adj,k-1)
            # b=dp(current,k-2)
            # print(a,b)
            d[current][k] += dp(adj, k - 1) - d[current][k - 2]

        return d[current][k]

    for i in range(1, N + 1):
        d[i][0] = cows[i]

    # K가 1일때 특정 칸에 몰릴 수 있는 최대치는 원래 있는 소 + 1칸 떨어진 소들이 다 그리로 모일때
    # d[node][1] = d[node][0] + sum(d[adj][0])
    for i in range(1, N + 1):
        d[i][1] = d[i][0]
        for adj in edges[i]:
            d[i][1] += d[adj][0]

    for i in range(1, N + 1):
        for j in range(2, K + 1):
            dp(i, j)

    for i in range(1, N + 1):
        print(d[i][K])


sol()
