from sys import stdin

N = int(stdin.readline())


def ans():

  dp = [0 for _ in range(100000 + 1)]

  dp[0] = 0
  dp[1] = dp[2] = dp[5] = dp[7] = 1
  dp[3] = dp[4] = dp[6] = 2

  for i in range(8, N + 1):
    dp[i] = min(dp[i - 7], dp[i - 5], dp[i - 2], dp[i - 1]) + 1

  return dp[N]


print(ans())