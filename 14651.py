from sys import stdin

N = int(stdin.readline())

dp = [[0] for _ in range(N+1)]
mod = int(1e9 + 9)


def ans():
  dp[1]=0
  if N>=2:
    dp[2]=2

  for i in range(3,N+1):
    dp[i]=(dp[i-1]*3)%mod
  return dp[N]


print(ans())