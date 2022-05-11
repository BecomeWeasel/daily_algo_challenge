from sys import stdin

T = int(stdin.readline())

modulo = 1000000009

dp = [[0 for _ in range(4)] for _ in range(1000000 + 1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for k in range(4, 1000000 + 1):
    dp[k] = (dp[k - 1] + dp[k - 2] + dp[k - 3]) % modulo

for _ in range(T):
    n = int(stdin.readline())
    print(dp[n])
