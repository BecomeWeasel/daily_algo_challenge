from sys import stdin

N = int(stdin.readline())


def sol():
    dp = [0 for _ in range(15 + 1)]

    T = [0 for _ in range(N+1)]
    P = [0 for _ in range(N+1)]

    for i in range(N):
        t, p = map(int, stdin.readline().split())
        T[i + 1], P[i + 1] = t, p

    for n in range(1, N + 1):
        # 오늘 딱 끝나는 것 중에서
        # ( x+T[x]-1 == N -> 3일째 업무가 2일이 걸리면 3,4일 하고 4일에 종료)
        # 그 일을 하기 전 최댓값과 그 일을 하게 되었을때 최댓값을 더하면
        # 오늘까지 번 돈의 최댓값이 될 수 있음
        candidate = [dp[n - T[x]] + P[x] for x, k in enumerate(T) if x + T[x] - 1 == n]

        # 오늘 안에 딱 끝나는게 한개도 없다면
        # 어제 번 돈의 최댓값하고 같다

        # 오늘 끝나는게 있어도 어제까지 번돈이 더클수도 있음
        dp[n] = max(max(candidate), dp[n - 1]) if len(candidate) != 0 else dp[n - 1]

    return dp[N]


print(sol())