from sys import stdin

def sol():
    N=int(stdin.readline())
    dp=[float('inf') for _ in range(5000+1)]

    # dp[0]=dp[1]=dp[2]=dp[4]=-1

    dp[3]=dp[5]=1

    for n in range(6,N+1):
        if dp[n-3]==float('inf') and dp[n-5]==float('inf'):
            continue
        else:
            dp[n]=min(dp[n-3],dp[n-5])+1

    return dp[N] if dp[N]!=float('inf') else -1

print(sol())