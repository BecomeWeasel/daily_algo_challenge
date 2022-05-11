from sys import stdin
from collections import defaultdict

N, M = map(int, stdin.readline().split())


def sol():
    visit = defaultdict(int)
    numbers = list(map(int, stdin.readline().split()))
    numbers.sort()

    for num in numbers:
        visit[num] += 1

    def dfs(k, nums):
        nonlocal visit, numbers
        if k == M:
            print(" ".join(map(str, list(nums))))
            return

        for num in numbers:
            dfs(k + 1, nums[:] + [num])

    numbers = sorted(list(set(numbers)))

    for num in numbers:
        dfs(1, [num])


sol()
