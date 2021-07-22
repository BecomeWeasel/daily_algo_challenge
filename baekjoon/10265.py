# SCC의 요소 개수들의 합 혹은 SCC로 갈 수 있는 추가들도 더해서

# SCC들에 대해서 SCC 모두가 들어가거나
# SCC 요소 각각을 가리키는 추가적인 몇개가 더 들어갈 수 있음
# SCC의 개수를 P개라고한다면 , 최소 P개부터 들어갈 수 있음
# SCC 요소를 가리키는 추가적인 개수를 Q개라고 할때
# 한 개의 SCC에는 P~P+Q명 탑승가능
# 그 합들이 만들수 있는 K보다 작거나 같은 최댓값 -> 배낭 문제

from sys import stdin, setrecursionlimit
from collections import defaultdict

# pypy3에서는 필요하지 않으면 setrecursionlimit 사용 자제
# setrecursionlimit(10**7)

n, k = map(int, stdin.readline().split())


def sol():
    prefer = [-1] + list(map(int, stdin.readline().split()))

    visit = [0 for _ in range(n + 1)]
    scc_indicator = [0 for _ in range(n + 1)]
    SCC_min_max = defaultdict(int)
    SCC = []

    reversed_prefer = defaultdict(list)

    for src in range(1, n + 1):
        dest = prefer[src]
        reversed_prefer[dest].append(src)

    reversed_check = set()

    def scc_root_dfs(SCC_NUM, node):
        nonlocal SCC_min_max, reversed_prefer
        reversed_check.add(node)

        SCC_min_max[SCC_NUM][1] += 1

        for reversed_node in reversed_prefer[node]:
            if reversed_node not in reversed_check:
                scc_root_dfs(SCC_NUM, reversed_node)
        return

    def dfs(node, trace):
        nonlocal prefer, visit
        visit[node] += 1

        # visit[prefer[node]]가 0보다 크면 1번이라도 방문한것
        # 사이클 발견되면
        if visit[prefer[node]] > 0:
            if prefer[node] in trace:
                s_idx = trace.index(prefer[node])
                scc_elements = trace[s_idx:]

                # SCC 루트
                SCC.append(prefer[node])

                # 루트에서 역전한 그래프를 대상으로 DFS

                SCC_num = len(SCC)

                # SCC 요소의 길이와 , 확장된 SCC 요소의 길이
                # SCC_LEN[P]=[a,b]라면
                # P번 SCC에는 최소 a명이,
                # P번 확장 SCC에는 최대 b명
                SCC_min_max[SCC_num] = [len(scc_elements), 0]
                scc_root_dfs(SCC_num, prefer[node])

        else:
            visit[prefer[node]] += 1
            trace.append(prefer[node])
            dfs(prefer[node], trace)

    for node_num in range(1, n + 1):  # O(n)
        if visit[node_num] == 0:
            dfs(node_num, [node_num])

    SCC_min_max = list(SCC_min_max.values())
    # print("-----")
    # print(SCC_LEN)

    # '''

    dp=[[0 for _ in range(1001)] for _ in range(1001)]
    for i in range(len(SCC_min_max)):
        # minSCC : SCC의 크기
        # maxSCC : SCC에 달려있는 것들 (최대크기)
        minSCC, maxSCC = SCC_min_max[i][0], SCC_min_max[i][1]

        if minSCC > k:
            continue

        for j in range(k, -1, -1):
            dp[i][j]=dp[i-1][j]
            for w in range(minSCC, maxSCC + 1):
                if j - w >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + w)
    
    return dp[len(SCC_min_max) - 1][k]

    # '''
    '''
    dp = [False for _ in range(1001)]

    dp[0] = True

    for i in range(len(SCC_min_max)):
        for j in range(k, -1, -1):
            for w in range(SCC_min_max[i][1], SCC_min_max[i][0] - 1, -1):
                if j >= w:
                    dp[j] |= dp[j - w]

    for i in range(k + 1, -1, -1):
        if dp[i]:
            return i

    '''


print(sol())