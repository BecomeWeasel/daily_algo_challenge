from sys import stdin

N = int(stdin.readline())


def sol():
    rectangle_round = [-1 for _ in range(80 + 1)]
    rectangle_round[1] = 4
    fibo = [-1 for _ in range(80 + 1)]
    fibo[0] = 0
    fibo[1] = 1
    """ 
    # bottom-up
    for i in range(2, N + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        rectangle_round[i] = rectangle_round[i - 1] + fibo[i] * 2
    """

    # top-down
    def getFibo(N):
        nonlocal fibo

        if fibo[N] >= 0:
            return fibo[N]

        fibo[N] = getFibo(N - 1) + getFibo(N - 2)

        return fibo[N]

    def getRound(N):
        nonlocal rectangle_round

        if rectangle_round[N] >= 0:
            return rectangle_round[N]

        rectangle_round[N] = getRound(N - 1) + getFibo(N) * 2

        return rectangle_round[N]

    rectangle_round[N] = getRound(N)

    return rectangle_round[N]


print(sol())
