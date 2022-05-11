from sys import stdin
from bisect import bisect_left


def is_exist(l, key):
    idx = bisect_left(l, key)

    if l[idx] != key:
        return False
    return True


def sol():
    N = int(stdin.readline())
    numbers = list()

    for _ in range(N):
        numbers.append(int(stdin.readline()))

    numbers.sort()

    two_sum = list()

    for num1 in numbers:
        for num2 in numbers:
            two_sum.append(num1 + num2)

    answer = -float("inf")

    two_sum.sort()

    for k in numbers:
        for l in numbers:
            if is_exist(two_sum, l - k):
                answer = max(answer, l)

    return answer


print(sol())
