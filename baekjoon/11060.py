from sys import stdin

N=int(stdin.readline())


def sol():
    board=[-1]+list(map(int,stdin.readline().split()))

    dp=[float('inf') for _ in range(N+1)]

    dp[1]=0

    for n in range(1,N):
        for jump in range(board[n]+1):
            if n+jump<=N:
                dp[n+jump]=min(dp[n+jump],dp[n]+1)



    return dp[N] if dp[N]!=float('inf') else -1

print(sol())