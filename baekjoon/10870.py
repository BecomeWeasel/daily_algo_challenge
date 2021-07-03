from sys import stdin

N = int(stdin.readline())


def sol():
    MAX_LEN = 20
    dp = [-1 for _ in range(MAX_LEN + 1)]
    dp[0] = 0
    dp[1] = 1
    '''
    # bottom-up
    for i in range(2,N+1):
        dp[i]=dp[i-1]+dp[i-2]
    '''

    # top-down

    def getDP(n):
        nonlocal dp
        if dp[n] >= 0:
            return dp[n]

        dp[n] = getDP(n - 1) + getDP(n - 2)

        return dp[n]

    return getDP(N)


print(sol())