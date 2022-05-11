from sys import stdin

T = int(stdin.readline())


def sol():

    N = int(stdin.readline())
    dp = [-float("inf") for _ in range(1000)]

    numbers = list(map(int, stdin.readline().split()))
    dp[0] = numbers[0]

    for n in range(1, N):
        dp[n] = max(numbers[n], dp[n - 1] + numbers[n])

    return max(dp)


for _ in range(T):
    print(sol())
