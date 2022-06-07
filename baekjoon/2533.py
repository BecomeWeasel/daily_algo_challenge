from sys import stdin, setrecursionlimit

setrecursionlimit(10**6 + 50)

N = int(stdin.readline())


def sol():

    dp = [[0, 1] for _ in range(N + 1)]

    # 만약 내가 O면 내 자식들은 O X 상관 없음 아무거나 작은걸로
    # 근데 내가 X다? 내 자식들은 다 무조건 O여야함.
    # 내가 얼리어답터가 아니기때문에 내 자식들이 모두 나에게 아이디어를 퍼트려줘야 하기 때문임.

    # 그러니까
    # dp[N][0] : N이 X일때 N을 루트로 하는 서브트리에서 완성하기 위한 최솟값
    # dp[N][1] : N이 O일때 N을 루트로 하는 서브트리에서 완성하기 위한 최솟값

    # dp[N][0]= Sum(dp[child][1])
    # dp[N][1]= Sum(min(dp[child]))+1

    edges = [[] for _ in range(N + 1)]

    # 아무 노드나 잡고 시작해도 됨.
    # 양방향이니 무조건 아무 노드나 루트라고 할 수 있음.

    for _ in range(N - 1):
        a, b = map(int, stdin.readline().split())

        edges[a].append(b)
        edges[b].append(a)

    visit = [False for _ in range(N + 1)]

    def calc(node):
        nonlocal dp, visit, edges

        if visit[node]:
            return dp[node]

        visit[node] = True

        for adj in edges[node]:
            if visit[adj]:
                continue

            dp[node][0] += calc(adj)[1]
            dp[node][1] += min(calc(adj))
        # dp[node][1]+=1
        return dp[node]

    calc(1)

    return min(dp[1])


print(sol())
