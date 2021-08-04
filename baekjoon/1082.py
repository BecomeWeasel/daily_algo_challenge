from sys import stdin
from itertools import permutations


def sol():
    N = int(stdin.readline())

    cost = list(map(int, stdin.readline().split()))

    money = int(stdin.readline())

    dp = [-1 for _ in range(51)]

    for n in range(money + 1):
        for num in range(N):
            if n + cost[num] <= money:
                if dp[n] == -1:
                    dp[n + cost[num]] = max(dp[n + cost[num]], num)
                else:
                    dp[n + cost[num]] = max(dp[n + cost[num]], int(str(dp[n]) + str(num)))

    return max(dp)


print(sol())