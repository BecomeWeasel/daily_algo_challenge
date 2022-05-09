from sys import stdin

n = int(stdin.readline())

m = int(stdin.readline())

# 시간복잡도 위주로 봐보자.

# 인접행렬을 쓴다고했을때, 도시의 개수만큼 3중 루프니까 n^3
# 그리고 인접리스트는 잘 모르겠는게,
# m이 최대 n^2이니까, 최대는 모든 노드가 연결되있는 상태일거임.
# density가 높은 상태일거임
# n<=100이니까 최대 100^3하면, 100만 충분히 가능


def sol():
    # 엣지들이 양방향이라는 명확한 언급이 없음.
    cost = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]

    # 문제의 존나 큰 함정
    # a->b 이게 여러개일수잇고,
    # 그때 최솟값만 저장하자.

    # 그니까 제발 문제를 잘읽자 ㅠ
    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())

        cost[a][b] = min(cost[a][b], c)

    for i in range(1, n + 1):
        cost[i][i] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                if cost[j][k] > cost[j][i] + cost[i][k]:
                    cost[j][k] = cost[j][i] + cost[i][k]

    for i in range(1, n + 1):
        result = []
        for j in range(1, n + 1):
            if cost[i][j] == float("inf"):
                cost[i][j] = 0
            result.append(cost[i][j])

        print(" ".join(map(str, result)))


sol()
