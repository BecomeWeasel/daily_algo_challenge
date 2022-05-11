from sys import stdin


def sol():
    N, M = map(int, stdin.readline().split())

    trees = list(map(int, stdin.readline().split()))

    left = 0
    right = max(trees)

    answer = -float("inf")

    while left <= right:
        mid = (left + right) // 2

        total = sum(max(0, tree - mid) for tree in trees)

        if total >= M:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    return answer


print(sol())
