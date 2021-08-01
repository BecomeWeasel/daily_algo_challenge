from sys import stdin


def sol():
    N = int(stdin.readline())

    L = list(map(int, stdin.readline().split()))
    R = list(map(int, stdin.readline().split()))

    L.reverse()
    R.reverse()

    L = [-1] + L
    R = [-1] + R

    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    dp[N][N]=0
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            # dp[i][j]가 0보다 작다는건 
            # 이건 계산이 애초에 안되니까
            # 왼쪽 i장 오른쪽 j장은 나올수 없는 상황인것
            if not dp[i][j]>=0:
                continue
            if L[i] > R[j]:
                dp[i][j - 1] = max(dp[i][j] + R[j], dp[i][j - 1])

            dp[i - 1][j - 1] = max(dp[i-1][j-1],dp[i][j])
            dp[i - 1][j] = max(dp[i-1][j],dp[i][j])

    ret = 0


    for i in range(1, N + 1):
        ret = max(ret, dp[0][i])

    for j in range(1, N + 1):
        ret = max(ret, dp[j][0])
    return ret


print(sol())
