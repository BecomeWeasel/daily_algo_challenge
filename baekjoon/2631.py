from sys import stdin
from bisect import bisect_left


def sol():
    N = int(stdin.readline())

    numbers = list()

    for _ in range(N):
        numbers.append(int(stdin.readline()))

    C = [float("inf") for _ in range(N + 1)]
    C[0] = -float("inf")
    C[1] = numbers[0]

    length = 1

    for n in numbers:
        if C[length] < n:
            length += 1
            C[length] = n
        else:
            loc = bisect_left(C, n)
            C[loc] = n

    return N - length


print(sol())
