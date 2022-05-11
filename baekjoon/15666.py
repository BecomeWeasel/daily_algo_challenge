from sys import stdin
from collections import defaultdict

N, M = map(int, stdin.readline().split())


def sol():
    visit = defaultdict(int)
    numbers = list(map(int, stdin.readline().split()))
    numbers.sort()

    for num in numbers:
        visit[num] += 1

    def dfs(k, idx, nums):
        nonlocal visit, numbers
        if k == M:
            print(" ".join(map(str, list(nums))))
            return

        for i in range(idx, len(numbers)):
            num = numbers[i]
            dfs(k + 1, i, nums[:] + [num])

    numbers = sorted(list(set(numbers)))

    for idx, num in enumerate(numbers):
        dfs(1, idx, [num])


sol()
