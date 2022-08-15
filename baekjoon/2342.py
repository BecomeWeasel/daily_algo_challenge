from sys import stdin
from collections import deque

order = list(map(int, stdin.readline().split()))

order.insert(0, -1)


def resolver(foot, next_step):
    if foot == next_step:
        return 1
    elif foot == 0:
        return 2
    else:
        # 반대쪽
        if abs(next_step - foot) == 2:
            return 4
        # 인접지점일때
        else:
            return 3


dp = [[[float("inf") for right in range(5)] for left in range(5)] for _ in range(len(order))]

dp[1][0][0] = 0

idx = 1
while idx < len(order) - 1:

    next_step = order[idx]

    # print(idx,next_step)

    for l in range(5):
        for r in range(5):
            # 왼발 그대로
            if next_step == l:
                dp[idx + 1][next_step][r] = min(
                    dp[idx + 1][next_step][r], dp[idx][l][r] + resolver(l, next_step)
                )
            # 오른발 그대로
            elif next_step == r:
                dp[idx + 1][l][next_step] = min(
                    dp[idx + 1][l][next_step], dp[idx][l][r] + resolver(r, next_step)
                )
            else:
                dp[idx + 1][next_step][r] = min(
                    dp[idx + 1][next_step][r], dp[idx][l][r] + resolver(l, next_step)
                )
                dp[idx + 1][l][next_step] = min(
                    dp[idx + 1][l][next_step], dp[idx][l][r] + resolver(r, next_step)
                )
    idx += 1
answer = float("inf")
for l in range(5):
    for r in range(5):
        answer = min(answer, dp[idx][l][r])


print(answer)
