from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    soil = list(map(int, stdin.readline().split()))
    acc = [0 for _ in range(N + 1)]

    for _ in range(M):
        a, b, k = map(int, stdin.readline().split())

        acc[a - 1] += k
        acc[b] += -k

    for i in range(N):
        acc[i + 1] += acc[i]
        soil[i] += acc[i]

    return " ".join(map(str, soil))


print(sol())
