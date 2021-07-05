from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    # visit = set()
    numbers = list(map(int, stdin.readline().split()))
    numbers.sort()

    def dfs(k, nums):
        nonlocal numbers
        if k == M:
            print(' '.join(map(str, list(nums))))
            return

        for num in numbers:
            dfs(k + 1, nums[:] + [num])

    for num in numbers:
        dfs(1, [num])


sol()