from sys import stdin

N, M = map(int, stdin.readline().split())


def sol():
    numbers = list(map(int, stdin.readline().split()))

    dp = [0 for _ in range(100000 + 1)]

    dp[1] = numbers[0]

    for n in range(1, N + 1):
        dp[n] = dp[n - 1] + numbers[n - 1]

    for _ in range(M):
        start, end = map(int, stdin.readline().split())
        print(dp[end] - dp[start - 1])


sol()