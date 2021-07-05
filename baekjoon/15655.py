from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    visit = set()
    numbers = list(map(int, stdin.readline().split()))
    numbers.sort()

    def dfs(k, idx, nums):
        nonlocal visit, numbers
        if k == M:
            print(' '.join(map(str, list(nums))))
            return

        for i in range(idx, len(numbers)):
            num = numbers[i]
            if num not in visit:
                visit.add(num)
                dfs(k + 1, i, nums[:] + [num])
                visit.remove(num)

    for idx, num in enumerate(numbers):
        visit.add(num)
        dfs(1, idx, [num])
        visit.remove(num)


sol()