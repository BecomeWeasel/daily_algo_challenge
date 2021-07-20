from sys import stdin

N = int(stdin.readline())


def sol():

    A = list(map(int, stdin.readline().split()))

    dp = [[-float('inf') for _ in range(2)] for _ in range(N)]

    dp[0][1] = A[0]

    for n in range(1, N):
        dp[n][0] = max(dp[n - 1][0], dp[n - 1][1])
        dp[n][1] = max(dp[n - 1][1] + A[n], A[n])

    return max(dp[N - 1])


print(sol())