from bisect import bisect_left
from sys import stdin

N = int(stdin.readline())


def sol():
    global N
    length = 0

    numbers = list(map(int, stdin.readline().split()))

    C = [-float("inf") for _ in range(N + 1)]

    for num in numbers:
        if C[length] < num:
            length += 1
            C[length] = num
        else:
            pos = bisect_left(C, num, 0, length)
            C[pos] = num

    return length


print(sol())
