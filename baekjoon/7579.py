from sys import stdin

N, M = map(int, stdin.readline().split())

memory = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))

# C를 최소화해서 m의 합이 M 이상으로 ..

# DFS를 하기에는 N이 너무 큼. 2^100이니, 백트래킹해서 쳐내더라도 많아보임

# 냅색 DP 해보자

# 근데 배열길이가 매우 길어지니 dict로 구현..?

# 좀 걸리는게 M바이트 이상이라는거지 M바이트만큼 정확히쓰는건 아닌데............
# DP 계산하면서 M바이트 이상일때 기록해두기

dp = [[-1 for _ in range(10001)] for _ in range(N + 1)]

dp[0][0] = 0
dp[0][cost[0]] = memory[0]

# answer= cost[0] if memory[0] >=M else 987654321

for i in range(N - 1):
    for j in range(10000):

        if j + cost[i + 1] <= 10000:
            # 지금 상태에서 다음 앱을 껏다켜서 메모리를 확보하거나
            dp[i + 1][j + cost[i + 1]] = max(dp[i + 1][j + cost[i + 1]], dp[i][j] + memory[i + 1])

            # 중간에 만족하는 C 비용 있으면 작은값을 기록
            # 근데 이렇게 안해도 되네
            # if dp[i+1][j+cost[i+1]]>=M:
            #     answer=min(answer,j+cost[i+1])
            # 암것도 안하거
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])


for j in range(10001):
    if dp[N - 1][j] >= M:
        print(j)
        break
