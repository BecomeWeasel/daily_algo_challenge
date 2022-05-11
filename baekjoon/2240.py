from sys import stdin

T, W = map(int, stdin.readline().split())


def sol():
    dp = [[[0 for _ in range(3)] for _ in range(31)] for _ in range(1001)]

    drop = [-1]

    for t in range(T):
        pos = int(stdin.readline())

        drop.append(pos)

    if drop[1] == 1:
        dp[1][0][1] = 1
    else:
        dp[1][1][2] = 1

    for i in range(2, T + 1):
        for k in range(W + 1):

            if drop[i] == 1:
                if k == 0:
                    dp[i][0][1] = dp[i - 1][0][1] + 1
                    continue

                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][2]) + 1
                dp[i][k][2] = max(dp[i - 1][k][2], dp[i - 1][k - 1][1])
            else:
                if k == 0:
                    dp[i][0][2] = dp[i - 1][0][2] + 1
                    continue

                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][2])
                dp[i][k][2] = max(dp[i - 1][k - 1][1], dp[i - 1][k][2]) + 1

    return max(max(dp[T]))


def sol2():

    T, W = map(int, stdin.readline().split())

    dp = [[[0 for _ in range(31)] for _ in range(2)] for _ in range(1001)]

    first_tree = [False for _ in range(1001)]
    second_tree = [False for _ in range(1001)]

    for t in range(T):
        pos = int(stdin.readline())

        if pos == 1:
            first_tree[t + 1] = True
        else:
            second_tree[t + 1] = True

    if first_tree[1]:
        dp[1][0][0] = 1
    else:
        dp[1][1][1] = 1

    for i in range(2, T + 1):
        for k in range(W + 1):
            if k == 0:
                dp[i][0][0] = dp[i - 1][0][0]
                dp[i][1][0] = dp[i - 1][1][0]
            else:
                dp[i][0][k] = max(dp[i - 1][0][k], dp[i - 1][1][k - 1])
                dp[i][1][k] = max(dp[i - 1][0][k - 1], dp[i - 1][1][k])

            if first_tree[i]:
                dp[i][0][k] += 1
            else:
                dp[i][1][k] += 1
    return max(max(dp[T]))


print(sol())

print(sol2())
