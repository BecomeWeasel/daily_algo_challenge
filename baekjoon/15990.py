from sys import stdin

T = int(stdin.readline())


def sol():
    dp = [[0, 0, 0, 0] for _ in range(100000 + 1)]

    dp[1] = [0, 1, 0, 0]
    dp[2] = [0, 0, 1, 0]
    dp[3] = [0, 1, 1, 1]

    for n in range(4, 100000 + 1):
        dp[n][1] = (dp[n - 1][2] + dp[n - 1][3])%(int(1e9)+9)
        dp[n][2] = dp[n - 2][1] + dp[n - 2][3]%(int(1e9)+9)
        dp[n][3] = dp[n - 3][1] + dp[n - 3][2]%(int(1e9)+9)
    
    for _ in range(T):
        N=int(stdin.readline())
        print(sum(dp[N])%(int(1e9)+9))
sol()
