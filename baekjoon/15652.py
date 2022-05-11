from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    visit = [False for _ in range(8 + 1)]

    def dfs(k, prev_num, nums):
        nonlocal visit
        if k == M:
            print(" ".join(map(str, list(nums))))
            return

        for i in range(prev_num, N + 1):
            dfs(k + 1, i, nums + str(i))

    for i in range(1, N + 1):
        dfs(1, i, str(i))


sol()
