from sys import stdin
from collections import deque

N = int(stdin.readline())


def ans():
    q = deque()
    print_list = list()
    for i in range(1, N + 1):
        q.append(i)

    while len(q) != 1:
        trash = q.popleft()
        print_list.append(trash)

        top = q.popleft()
        q.append(top)

    s = ""
    for c in print_list:
        s += str(c) + " "
    s += str(q.pop())
    print(s)


ans()
