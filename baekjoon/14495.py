from sys import stdin

N = int(stdin.readline())


def sol():
    fibo = [0 for _ in range(117)]

    fibo[1] = fibo[2] = fibo[3] = 1

    for n in range(4, N + 1):
        fibo[n] = fibo[n - 1] + fibo[n - 3]

    return fibo[N]


print(sol())
