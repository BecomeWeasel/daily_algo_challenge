from sys import stdin


def sol(N):
    numbers = []

    for _ in range(N):
        numbers.append(int(stdin.readline()))

    dp = [-float("inf") for _ in range(N)]

    dp[0] = numbers[0]

    for n in range(1, N):
        dp[n] = max(dp[n - 1] + numbers[n], numbers[n])

    return max(dp)


while True:
    N = int(stdin.readline())

    if N != 0:
        print(sol(N))
    else:
        break
