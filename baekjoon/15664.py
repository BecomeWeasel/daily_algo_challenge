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
            if visit[num] > 0:
                visit[num] -= 1
                dfs(k + 1, i, nums[:] + [num])
                visit[num] += 1

    numbers = sorted(list(set(numbers)))

    for idx, num in enumerate(numbers):
        visit[num] -= 1
        dfs(1, idx, [num])
        visit[num] += 1


sol()
