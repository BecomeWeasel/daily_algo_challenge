from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def sol():

    # 2<=N<=15

    # 이거를 유방향 그래프로 나타낸 상태로 생각해보자.

    # i번째 줄의 j번째수는 j번 예술가가 i번에게 그 그림을 살때의 가격이니 (c)
    # i->j : c로 나타내면,

    # 초기 lambda에서 시작해서 , 1번은 lambda에게 0원 (1->lambda : 0)

    # 이 상태에서 1번 조건을 만족하려면, 이전의 edge의 값보다는 더 크게...
    # 근데 같은 그림 두번이상 사는것은 안되니까 중복방문 비허용

    # 입력은 길이의 인접행렬임 ㅇㅇ

    # 그럼 결국에 가장 긴 거리를 찾는것임. DFS 사용해보자.

    # 엥 근데 61퍼까지는 올라가다가 시간초과가 나네................

    # 그럼 최대한 거리를 길게 하려면 어떻게 해야할까..?

    # 탐색할때 금액 차이 얼마 안나는애한테 먼저팔까..?
    # 근데 걔가 싸게사서 엄청 높게만 판다하면 의미가 없어
    # 가능성은 높아지겠지만...

    # K(K<=N)번째 사람일때 가격이 얼마인지 체크..?
    # 그래서 같은시점일때 이전보다 낮아지면 아예 X?

    # 근데 매번의 상황마다 , 누구를 방문했는지 여부가 달라져서 값이 달라질수 있는데..

    # N<=15니 bit 이용해서 표현해볼까...
    # 특정 비트일때 , 금액이 더 작아야하는..?

    N = int(stdin.readline())

    answer = 1

    price_matrix = []

    for _ in range(N):
        s = stdin.readline().rstrip()

        price_matrix.append(list(map(int, s)))

    # for r in price_matrix:
    #     print(r)

    def dfs(dist, current, prev_price, visit_bit, bit_status):
        nonlocal answer, price_matrix

        answer = max(answer, dist)

        for i in range(1, N):
            # if visit[i]:

            # continue
            if (
                prev_price <= price_matrix[current][i]
                and visit_bit[i][bit_status | (1 << i)] > price_matrix[current][i]
                and not (bit_status & (1 << i))
            ):
                # visit[i]=True
                visit_bit[i][bit_status | (1 << i)] = price_matrix[current][i]
                dfs(dist + 1, i, price_matrix[current][i], visit_bit, bit_status | (1 << i))
                # visit[i]=False

    visit_bit = [[987654321 for _ in range(2**15)] for _ in range(N)]
    bit_status = 1
    visit_bit[1][bit_status] = 0
    dfs(1, 0, 0, visit_bit, bit_status)

    return answer


print(sol())
