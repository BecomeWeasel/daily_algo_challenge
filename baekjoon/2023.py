from sys import stdin
from collections import deque


def isPrime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def bfs():
    q = deque()
    while result_list:
        q.append(result_list.popleft())

    while q:
        number = q.popleft()
        i = 1
        while i < 10:
            if isPrime(number * 10 + i):
                result_list.append(number * 10 + i)

            i += 2


def ans():
    for digit in range(1, N):
        bfs()

    for i in result_list:
        print(i)


result_list = deque()

result_list.append((2))
result_list.append((3))
result_list.append((5))
result_list.append((7))

N = int(stdin.readline())

ans()
