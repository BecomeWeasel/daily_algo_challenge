from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

N = int(stdin.readline())


def sol():
    cost = list(map(int, stdin.readline().split()))

    cost.insert(0, -1)

    edges = [list() for _ in range(N + 1)]

    for _ in range(N - 1):
        s, d = map(int, stdin.readline().split())

        edges[s].append(d)
        edges[d].append(s)

    # start_node, max_edges = -1, -1

    # for i in range(1, N):
    #     if len(edges[i]) > max_edges:
    #         max_edges = len(edges[i])
    #         start_node = i

    visit = [False for _ in range(N + 1)]

    dp = [[0, cost[i]] for i in range(N + 1)]

    def calc(node):
        nonlocal cost, dp, edges, visit

        # visit[node] = True

        # if dp[node][0] != 0 and dp[node][1] != 0:
        if visit[node]:
            return dp[node]

        visit[node] = True

        # 얜 리프노드
        # if len(edges[node]) == 1:
        #     dp[node][0] = 0
        #     dp[node][1] = cost[node]
        #     return dp[node]

        not_select_sum, select_sum = 0, 0

        for adj in edges[node]:
            if visit[adj]:
                continue

            # node를 포함하지 않는 최대값
            # 만약 node 불포함이면, 자식들은 선택할수도 , 안할수도있음
            # 최대값 가지는걸 고르자고.
            # 이게 문제의 3번조건을 위배하지 않는 이유는 어차피 최대값을 고른다는건
            # 문제 예시에서 6번 비선택시 자동으로 7번 선택된애로 골라버리는거
            not_select_sum += max(calc(adj))

            # node를 포함하는 최대값
            # 단 하나의 자식만을 선택하지는 않아도 되니 ...
            # 누적해서 더하지만, 만약에 node 선택시 자식은 무조건 선택하면 안됨
            select_sum += calc(adj)[0]

        dp[node] = [not_select_sum, select_sum + cost[node]]
        return dp[node]

    # 무조건 번갈아가면서 선택하는건아님
    calc(1)
    answer = -1
    for i in range(N + 1):
        answer = max(answer, dp[i][0], dp[i][1])

    return answer


print(sol())
