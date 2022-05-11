from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    visit = [False for _ in range(8 + 1)]

    def dfs(k, num, nums):
        nonlocal visit
        if k == M:
            print(" ".join(map(str, list(nums))))
            return

        for i in range(num + 1, N + 1):
            if not visit[i]:
                visit[i] = True
                dfs(k + 1, i, nums + str(i))
                visit[i] = False

    for i in range(1, N + 1):
        visit[i] = True
        dfs(1, i, str(i))
        visit[i] = False


sol()
