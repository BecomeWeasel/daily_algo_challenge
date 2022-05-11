from sys import stdin

T = int(stdin.readline())


def sol():
    N = int(stdin.readline())

    U = list(map(int, stdin.readline().split()))
    D = list(map(int, stdin.readline().split()))

    dp = [[0 for _ in range(3)] for _ in range(N)]

    dp[0][0] = 0
    dp[0][1] = U[0]
    dp[0][2] = D[0]

    for n in range(1, N):
        dp[n][0] = max(dp[n - 1])
        dp[n][1] = max(dp[n - 1][0], dp[n - 1][2]) + U[n]
        dp[n][2] = max(dp[n - 1][0], dp[n - 1][1]) + D[n]

    return max(dp[n])


for _ in range(T):
    print(sol())
