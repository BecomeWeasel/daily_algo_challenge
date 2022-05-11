from sys import stdin
from bisect import bisect_left


def sol():
    # 이분탐색
    N, M = map(int, stdin.readline().split())

    numbers = list()

    answer = float("inf")

    for _ in range(N):
        numbers.append(int(stdin.readline()))

    numbers.sort()

    def bisect_solve(numbers: list, idx: int) -> None:
        nonlocal M, answer
        l, r = idx - 1, N - 1

        while l + 1 < r:
            mid = (l + r) // 2

            if numbers[mid] - numbers[idx] >= M:
                r = mid
            else:
                l = mid

        if numbers[r] - numbers[idx] < answer and numbers[r] - numbers[idx] >= M:
            answer = numbers[r] - numbers[idx]

    for idx in range(N):
        bisect_solve(numbers, idx)

    return answer


def two_pointer():
    # 투포인터
    N, M = map(int, stdin.readline().split())

    numbers = list()

    answer = float("inf")

    for _ in range(N):
        numbers.append(int(stdin.readline()))

    numbers.sort()

    st, en = 0, 0

    while st < N and en < N:

        if numbers[en] - numbers[st] >= M:
            answer = min(answer, numbers[en] - numbers[st])
            st += 1
        else:
            en += 1
    return answer


# print(sol())
print(two_pointer())
