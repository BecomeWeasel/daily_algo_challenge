from sys import stdin

C, N = map(int, stdin.readline().split())


def sol():
    dp = [float("inf") for _ in range(2000)]

    dp[0] = 0

    cost, people = [], []
    for _ in range(N):
        c, p_ = map(int, stdin.readline().split())
        cost.append(c)
        people.append(p_)

    for n in range(C + 1):
        for c, p in zip(cost, people):
            dp[n + p] = min(dp[n + p], dp[n] + c)

    return min(dp[C:2000])


print(sol())
