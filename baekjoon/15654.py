from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    visit = set()
    numbers = list(map(int, stdin.readline().split()))
    numbers.sort()

    def dfs(k, nums):
        nonlocal visit, numbers
        if k == M:
            print(" ".join(map(str, list(nums))))
            return

        for num in numbers:
            if num not in visit:
                visit.add(num)
                dfs(k + 1, nums[:] + [num])
                visit.remove(num)

    for num in numbers:
        visit.add(num)
        dfs(1, [num])
        visit.remove(num)


sol()
