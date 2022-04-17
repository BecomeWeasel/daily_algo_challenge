from curses import nonl
from os import stat
from sys import stdin


def sol():

    # A번째 발전소를 켜기 위해 드는 비용은
    # X<- 0~N , X!=A : min(dp[X][A])
    # 그럼 X번째 발전소 켜기 위해 드는 비용은
    # Y<- 0~N , Y!=X , Y!=A : min(dp[Y][X])
    # 이중에서 계속 타다가 언제 멈추냐면,
    # 실제로 켜져있는 발전소 만나면 멈춤.
    # 거기서부터 올라가면 되니까 ..

    # 3
    # 0 10 11
    # 10 0 12
    # 12 13 0
    # YNN
    # 3

    # 에서 해보자.
    # 0번째 발전소 켜는 비용은 고려 X 왜냐면 이미 켜져있음 따라서 dp[0][0]=0

    # 1번째 발전소 켜는 비용은 min(dp[0][1],dp[2][1])
    # dp[0][1]은 간단하게 계산가능 이미 켜져있으니 cost[0][1] = 10

    # dp[2][1]은 2번 발전소가 안켜져있으니,
    # 2번 발전소 값 먼저 계산하자
    # 2번재 발전소 켜는 비용은
    # min(dp[0][2],dp[1][2])
    # dp[0][2]은 간단하게 cost[0][2] = 13
    # dp[1][2]은 1번 켜야하는 데드락 상태이니 결국은 결정못하는 상태임 그럼 일단
    # 2번 켜는 방법은 현재로썬 최소가 13임

    # 그럼 1번째 발전소 켜는 비용은 10임.

    # 그럼 2번째 발전소 켜는 비용 다시 고려하면,
    # min(dp[0][2],dp[1][2])
    # dp[0][2]은 간단하게 cost[0][2] = 13
    # dp[1][2]=dp[1] + cost[1][2]=10+12 = 22
    # 둘중에서 작은 13 고름.

    # 이게 발전소끼리 꼬리에 꼬리를 무는 상황이 생길수 있으니까 닭 vs 달걀
    # 연쇄적으로 켜지는 거 고려하지 말아야하나?

    # 근데 약간 위상정렬 느낌도 나긴한다
    # 0번 켜져있고 1,2,3 다 꺼져있다고 해보자.

    # 이때 0->1->2,3 일수도 있고 0->1->2->3 일수도 있음

    # 그럼 반대로 아예 초기에 켜져있는 것에서부터 시작을 해서
    # 일단 다켜볼까
    # 왜냐면 모든 발전소는 켜져있는곳에서만 켜지니까 ..
    # 그리고 이미 초기에 켜져있는 발전소를 다른데서 끌 필요는 없음

    # 3
    # 0 10 11
    # 10 0 12
    # 12 13 0
    # YNN
    # 3

    # 이러면 각각 초기 비용은 0,10,11

    # initial_dp=[inf for _ in range(N)]

    # # for i in range(N):
    #     # dp[i][i]=0

    # for i in range(N):
    #     if on[i]:
    #         initial_dp[i]=0
    #         for j in range(N):
    #             if not on[j]:
    #                 # 다른곳에서 여기를 켜는게 더 비용이 낮을수도 있으니
    #                 initial_dp[j]=min(initial_dp[j],cost[i][j])

    # 이랬을때, depth로 보자.
    # depth가 1이라는 말은 첨부터 켜진 발전소에서 바로 켜는걸 의미
    # depth가 N이면, 내 앞에 발전소들 N개를 거쳐서 내가 켜졌다는 것
    # 그럼 depth가 1인거랑 , depth가 1보다 큰거랑 비교해보는게 맞을듯

    # 3
    # 0 2 4
    # 2 0 3
    # 4 3 0
    # YNN

    # 0번이 1번,2번 다 켜면 각자 초기 비용은 0,2,4

    # 근데 만약 2번이 1번을 켠다음에 켜면 드는 비용은 3

    # 2+4 vs 2+3

    # 근데 순서가 계속 바뀌어서 문제라면
    # 걍순서 정해주는게 어떰?

    # 정확히는 켜질 발전소를 미리정하는거임

    # 왜냐면 P개만 켜면 되니까

    # 그럼 결국에 구하는건 처음으로 켜져잇는발전소에서 몇번을 켤지 결정

    # 그러면 발전소 켜진 상태를 비트로 나타내고 , 아까 위에서 쓴 로직 구현하자

    # 그리고 발전소 켜진 애에서부터 거꾸로 역추적하자.

    inf = 98765432198764321
    N = int(stdin.readline())

    cost = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        cost[i] = list(map(int, stdin.readline().split()))

    temp = stdin.readline()
    status = []

    for i in range(N):
        status.append(True if temp[i] == 'Y' else False)

    # 표현할수 있는 경우의 수를 생각하면,
    # 발전소가 N개니까 상태는 2^N개
    dp = [inf for _ in range(2**N)]

    plant_count = 0
    P = int(stdin.readline())

    # 근데 상태인 status는 0이 맨왼쪽이다.
    # 그니까 거꾸로 읽어가면서 하자

    # YNN -> 001
    # NYNN -> 0010
    # NNY -> 100

    status_bit = 0

    for on in status[::-1]:
        # 일단 한칸 늘려주고
        status_bit <<= 1

        if on:
            status_bit |= 1
            # 만약에 처음부터 P개 넘으면 계산 필요 X
            plant_count += 1

    # print(status_bit)
    def calc(plant_count, bit_status):
        nonlocal N, P, dp, inf

        # 만약 이제 다켜진 상태라면  더이상 돈 쓸필요가 없음

        if plant_count >= P:
            return 0

        # 이미 이 상태는 어디선가 계싼했음
        if dp[bit_status] != inf:
            return dp[bit_status]

        for on in range(N):
            # 먼저 켜져 있는 발전소를 찾자
            if bit_status & (1<<on):
                # 그 다음에 이제 켤 발전소를 정하자
                for off in range(N):
                    if off == on: continue
                    # 아무거나 꺼져 있는 발전소를 찾자
                    if not (bit_status & (1 << off)):
                        # 꺼진 발전소가 켜진 bit 상황에서
                        # 원래 켜져있는 발전소가 지금 꺼져잇는 발전소를 켜는 비용 더하기

                        # 왜이렇게 하냐면, off 인 발전소를 on을 이용했을때의 비용은
                        # off가 켜져있는 상황에서 만들어지는 거임

                        # 즉 off 상황을 X, 그게 켜진 상황을 Y라 하면,

                        # X=Y+(off->on에서의 전환 비용)
                        dp[bit_status] = min(dp[bit_status], calc(plant_count + 1, bit_status | (1 << off)) + cost[on][off])

        # 이제 이걸 다 계산해주면,
        # 특정 발전소가 켜져있을때 어떤 값으로 켜져있었는지 알 수 있다.

        return dp[bit_status]

    dp[status_bit] = calc(plant_count, status_bit)

    if dp[status_bit] == inf:
        return -1
    else:
        return dp[status_bit]


print(sol())
