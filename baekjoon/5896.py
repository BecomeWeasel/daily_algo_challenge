from cProfile import label
from select import select
from sys import stdin
import heapq as hq


def sol():
    N, num_of_coupon, money = map(int, stdin.readline().split())

    cows = []

    for _ in range(N):
        p, c = map(int, stdin.readline().split())

        cows.append((p, c))

    # cows_sort_by_low_coupon=sorted(cows,key=lambda x:(x[1],x[0]))

    hq.heapify(cows)

    coupon_selected = []

    # 강민이 힌트가 쿠폰으로 일단 산놈은 계속 들고가야한다했음
    # 내생각인데 쿠폰으로 싸게 산놈의 원래 가격을 x라고 해보고, 쿠폰 가격을 y라고 해보자

    # 그러면 어차피 다른 쿠폰으로 싸게 살 수 있는 놈이 있다고 해도
    # 언젠가는 그게 한계가 있음

    # 예를 들어서 다른 싼놈을 a,b라고 해볼때

    # x+b vs y+a 해보자는거임

    # 전자는 쿠폰 취소하고 일반가로 사는거임
    # 후자는 쿠폰그대로 쓰는거임

    # 근데 저게 언제오냐면 a<=b 이건 항상 성립함

    # 그러니까 x가 아무리 비싸도 언젠가는 b1<=b2<=....x<bk 인 구간이 온다는거임
    # 즉, 이 소는 사실 쿠폰 안써도 쿠폰 쓴놈보다 쌀수가 있다라는거

    # 그러니까 원래 쿠폰으로 사기로 마음먹은애는 바꿀수는 있어도 빠지면은 안됨.
    # 원래 쿠폰으로 샀을때 싼놈은 원래가격도 싸다는거니까

    # 그럼 일단 쿠폰으로 다산다음에 그 선택된 놈들중에서 교체해도 젤 타격이 적은 소
    # 그니까 원래 가격이 젤 싼애를 골라서 양자 비교하자

    # 일단은 쿠폰을쓰는게 이득이거든요 그니까 쿠폰먼저 써봅시다
    # 그리고 모든 소들을 다 탐색해야해요 시발이건맞겟지

    cows.sort(key=lambda x: (x[1], x[0]))

    coupon_selected = []

    coupon_buy = 0
    normal_buy = 0

    # 그리고 원래 가격자체가 싼애는 쿠폰가격도 쌀 가능성이 높음.

    for i in range(N):
        # 아직 쿠폰 덜썼다면 일단 쿠폰으로 사셈
        if num_of_coupon > 0:
            target_p, target_c = cows[i]
            if money - target_c < 0:
                break
            num_of_coupon -= 1
            money -= target_c

            # 이제 이 소새끼는 쿠폰으로 산거임

            # 그런다음에 이제 힙큐에 넣어주자
            hq.heappush(coupon_selected, (target_p, target_c))
            coupon_buy += 1
        # 이제 쿠폰 다떨어졌음 그럼 이젠 젤 만만한애 꺼내서 조져야함
        else:
            head_p, head_c = hq.heappop(coupon_selected)

            # 그냥 무지성구매했을때
            # 이게 0보다 크면 일단 사도댐
            # 근데 0보다 작으면 안댐; 못삼

            # 쿠폰 번복했을때 가격 젤 만만한 소의 원래가격 + 새로운 소의 쿠폰 가격
            change = head_p + cows[i][1]

            keep = head_c + cows[i][0]

            # 만약 이번 소는 현금으로도 못사고 , 환불받은다음에 재구매할 돈이 안되면
            if money < cows[i][0] and money + head_c < head_p + cows[i][1]:
                # 다시 넣어주기
                hq.heappush(coupon_selected, (head_p, head_c))
                continue
            # 반대로 무슨 짓을 해도 소를 살 수는 있으면
            else:
                # 번복하는게 더 낫다
                if change < keep:
                    # 원래 소 값 환불 + 현금가지불 + 새로운 소 쿠폰가 지불
                    money += head_c - head_p - cows[i][1]

                    # 새소를 선택해준다
                    hq.heappush(coupon_selected, (cows[i]))
                    # 이전 소는 넣어주면 안됨 # 얘는 한번당한애임
                    coupon_buy += 1
                # 그냥 안바꾸는게 낫고 새로 소살돈도 있으면 걍 현금으로 산다
                else:
                    money -= cows[i][0]
                    normal_buy += 1

                    # 다시 넣어주기
                    hq.heappush(coupon_selected, (head_p, head_c))

    # 카카시 전 풀이
    # 일단 쿠폰으로 싼거 다산다음에
    # 쿠폰으로 산놈들중에 가격싼애로 정렬해서
    # 아직 못산애들 하고
    # 쿠폰으로 산 애를 A, 못산애를 B라고 하면
    # A.c+B.p vs A.p+B.c
    # 해서 후자가 더 작으면, 바꾸는게 더 이득아님?
    # 그래서 money+A.c+A.p-B.c
    # 대신에 이게 0보다 작으면 안됨
    # 만약 후자가 더 크면
    # 다음 산놈애 대해서 시도하자

    # 아존나아깝다 다풀었는데,,,,우선순위큐

    return coupon_buy + normal_buy


print(sol())
