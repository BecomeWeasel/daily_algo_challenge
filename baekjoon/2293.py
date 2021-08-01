from sys import stdin

n, k = map(int, stdin.readline().split())


def sol():

    dp = [0 for _ in range(100001)]
    dp[0] = 1
    coins = []
    for _ in range(n):
        coins.append(int(stdin.readline()))

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]
    # print(dp[1:k+1])
    return dp[k]


print(sol())