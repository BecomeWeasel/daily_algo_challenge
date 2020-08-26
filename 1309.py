from sys import stdin


def ans():
  dp[1][0] = 1
  dp[1][1] = 1
  dp[1][2] = 1

  for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % mod

  return (dp[N][0] + dp[N][1] + dp[N][2]) % mod


mod = 9901
N = int(stdin.readline())
dp = [[0, 0, 0] for _ in range(N + 1)]
print(ans())
