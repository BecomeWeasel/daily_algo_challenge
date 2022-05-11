from sys import stdin

T = int(stdin.readline())


def sol():
    L, N = map(int, stdin.readline().split())
    pos = []
    for _ in range(N):
        pos.append(int(stdin.readline()))

    pos.sort()

    min_time, max_time = 0, -1

    for i in range(N):
        min_time = max(min_time, min(pos[i], L - pos[i]))
        max_time = max(max_time, max(pos[i], L - pos[i]))

    return min_time, max_time


for _ in range(T):
    print(" ".join(map(str, sol())))
