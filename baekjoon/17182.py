from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


N, K = map(int, stdin.readline().split())


def sol():
    edges = []

    for _ in range(N):
        edges.append(list(map(int, stdin.readline().split())))

    cost = [[float("inf") for _ in range(N)] for _ in range(2**N)]

    # 2<=N<=10 , 0<=K<=N

    # N이 작은데 맹점이 최악은 모든 노드가 서로서로 연결되었을때
    # 한번갈때 선택지가 계속 N개에서 안줄어들수잇지않나

    # 중복방문가능하니까 .. 물론 핑퐁하는경우는 없을거임

    # 끝을 체크해줘야함.
    # 끝이 언제냐면 모든 행성 방문했을때임.

    # 근데 단순히 visited로 체크하면안됨.

    # 왜냐면 중복방문이 가능하니까

    # 그렇다고 카운트만 찍어주기에는 순서가 정해져있지않음.

    # 그러니까 비트마스크로 쓸거임
    # N이 최대 10이니까 1024로 충분함

    # 모든 중복방문가능한데
    # 생각해보자. 진짜 중복방문 다 열어주면 난리남
    #
    # 지금 방문이 이전 방문(같은 비트상태로 표현)보다 더 최소시간을 가질때만
    # 방문하게해야됨 ㅇㅇ
    # 만약에 그게아니라면 바로 나가버림
    #
    # 이렇게 경우의수 쳐내면서 마지막 값이 결국 최소시간일꺼임
    # 최댓값은 cost[2^n-1]안에 들어있는거중 최소 ㅇㅇ

    # 근데 이게 중복방문허용하니까 1->0->3->0->2 처럼 의미없는 움직임이 잇어보이긴함
    # 근데 무조건 답에는 들어간단말이지?
    # 대신에 세번째 행성인 3이랑, 그다음 0이랑 차이점이 분명히 상태가 달라진거임 ㅇㅇ

    # 그래서 cost를 2차원으로 두자

    init = 1 << K

    cost[init][K] = 0

    def is_end(bit):
        if bit == 2**N - 1:
            return True
        return False

    def dfs(node, bit, time):
        nonlocal cost, edges

        if is_end(bit):
            cost[bit][node] = min(cost[bit][node], time)
            return

        for i in range(N):
            # 다시 갈필요는 없잔아
            if node == i:
                continue

            if time + edges[node][i] < cost[bit | (1 << i)][i]:
                cost[bit | (1 << i)][i] = time + edges[node][i]
                dfs(i, bit | (1 << i), time + edges[node][i])

    dfs(K, init, 0)

    # def calc(bit):
    #     nonlocal cost,edges

    #     if cost[bit]!=float('inf'):
    #         return cost[bit]

    #     for i in range(N):
    #         # 만약에 i번째가 방문된상태라면,
    #         # 나머지 방문한곳에서 거기를 방문한거임.
    #         # 역산해보자.
    #         if (bit &(1<<i)):
    #             for j in range(N):
    #                 if i==j: continue

    #                 if (bit&(1<<j)):
    #                     cost[bit]=min(cost[bit],edges[j][i]+calc(bit^(1<<i)))

    #     return cost[bit]

    return min(cost[2**N - 1])
    # return calc(2**N-1)


print(sol())
