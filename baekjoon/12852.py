from sys import stdin

N = int(stdin.readline())


def sol():

    dp = [float("inf") for _ in range(int(1e6) + 1)]
    pre = [0 for _ in range(int(1e6) + 1)]

    dp[0] = 0
    dp[1] = 0
    pre[1] = 0

    for n in range(2, N + 1):
        dp[n] = dp[n - 1] + 1
        pre[n] = n - 1

        if n % 2 == 0:
            if dp[n // 2] + 1 < dp[n]:
                dp[n] = dp[n // 2] + 1
                pre[n] = n // 2

        if n % 3 == 0:
            if dp[n // 3] + 1 < dp[n]:
                dp[n] = dp[n // 3] + 1
                pre[n] = n // 3

    print(dp[N])
    curr = N
    result = [curr]
    while curr != 1:
        curr = pre[curr]

        result.append(curr)

    print(" ".join(map(str, result)))


sol()
