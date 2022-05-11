from sys import stdin


def sol():
    N = int(stdin.readline())

    path = ["X"] + list(stdin.readline().rstrip())

    dp = [float("inf") for _ in range(N + 1)]

    dp[1] = 0

    for n in range(1, N):
        for k in range(1, N):
            if n + k > N:
                break
            if path[n] == "B" and path[n + k] == "O":
                dp[n + k] = min(dp[n + k], dp[n] + k * k)
            elif path[n] == "O" and path[n + k] == "J":
                dp[n + k] = min(dp[n + k], dp[n] + k * k)
            elif path[n] == "J" and path[n + k] == "B":
                dp[n + k] = min(dp[n + k], dp[n] + k * k)

    return dp[N] if dp[N] != float("inf") else -1


print(sol())
