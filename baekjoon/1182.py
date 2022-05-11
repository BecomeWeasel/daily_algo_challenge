from sys import stdin

N, S = map(int, stdin.readline().split())


def sol():
    global N, S
    count = 0
    numbers = list(map(int, stdin.readline().split()))

    def dfs(step, idx, total):
        nonlocal count, numbers
        if step == N:
            if total == S:
                # print(nums)
                count += 1
            return

        dfs(step + 1, idx + 1, total + numbers[idx + 1])
        dfs(step + 1, idx + 1, total)

    dfs(1, 0, numbers[0])
    dfs(1, 0, 0)

    return count if S != 0 else count - 1


print(sol())
