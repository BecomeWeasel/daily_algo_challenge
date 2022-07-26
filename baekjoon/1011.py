from sys import stdin

T = int(stdin.readline())

for i in range(T):
    src, dest = map(int, stdin.readline().split())

    dist = dest - src

    N = 0

    while True:
        if dist <= N * (N + 1):
            break
        N += 1

    print(N * 2 - 1 if dist <= N**2 else N * 2)
