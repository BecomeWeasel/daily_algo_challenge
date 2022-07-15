from sys import stdin
import heapq as hq

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(stdin.readline())
parent = [i for i in range(N)]


def sol():
    global N, parent

    # 일단 트리임 .................

    # 그다음에 플로이드 와샬을 수행한 뒤의 행렬에서 재밌는 점은,

    # v에서의 어느 점으로의 거리 중 가장작은건, 무조건 원래부터 잇엇다는거임

    # 최소값은 무조건 원래 엣지를 의미함

    # 근데 그러면 다른건 해당안되냐 했을때, 그건 아님 . 될수도 안될수도

    # 다만 확실한건 무조건 원래부터 있엇다는거는 가장 작은 거리의 것이다~

    # 근데 그러면 간선들이 하나씩만 골라지니
    # 이전에 선택안되었던 것들중에서 후보를 골라야하는데 ㅅㅂ 어케고르지

    # 근데 트리니까 , 경로가 유일한..? 이거 그냥 크루스칼돌리면 된다
    # 말이 어렵게 나와있어서 그렇지 실제로는 크루스칼인듯

    board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N - 1):
        dist = list(map(int, stdin.readline().split()))

        for j in range(i + 1, N):
            board[i][j] = dist[j - (i + 1)]
        # print(board[i])

    count = 0

    # pq_per_node=[[] for _ in range(N)]

    pq_edge = []

    answer_tree = [[] for _ in range(N)]

    # for i in range(N):
    #     for j in range(N):

    #         board[j][i]=board[i][j]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                continue

            pq_edge.append((board[i][j], i, j))

    # for i in range(N):
    #     for j in range(N):
    #         if board[i][j]==0:
    #             continue

    #         pq_per_node[i].append((board[i][j],j))
    #     hq.heapify(pq_per_node[i])

    # for r in board:
    #     print(r)

    hq.heapify(pq_edge)

    while count < N - 1:
        # for src in range(N):
        #     dist,dest=hq.heappop(pq_edge)

        #     # 같은 집합이 아니라면
        #     if find_parent(parent,src)!=find_parent(parent,dest):
        #         union_parent(parent,src,dest)
        #         count+=1
        #         answer_tree[src].append(dest)
        #         answer_tree[dest].append(src)
        #     else:
        #         continue
        dist, src, dest = hq.heappop(pq_edge)

        if find_parent(parent, src) != find_parent(parent, dest):
            union_parent(parent, src, dest)
            count += 1
            answer_tree[src].append(dest)
            answer_tree[dest].append(src)

    for i in range(N):
        print(len(answer_tree[i]), " ".join(map(str, sorted(map(lambda x: x + 1, answer_tree[i])))))


sol()
