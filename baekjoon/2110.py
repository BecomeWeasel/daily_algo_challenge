from sys import stdin


N,C=map(int,stdin.readline().split())

def sol():


    houses=list()

    for _ in range(N):
        houses.append(int(stdin.readline()))
    
    ## 그냥 naitve하게 짠다고 생각해보자.

    # 집 좌표가 같은곳은 없다고 했으므로
    # N개중에서 C개 선택해서 그 값들 사이에서 최대 값...
    # 근데 N이 20만임 절대불가임
    # 최악은 (20만)C(10만)
    # 그러면 20만!/10만!
    
    # 그러니까 거리를 정해놓고 가자
    # 왜냐면 지금 거리가 계속 변경되니까

    # 가장 짧은 거리는 차이가 가장 적은 집 사이의 거리
    # 가장 긴 거리는 딱 두개만 설치할때 양 끝
    # 
    # 만약에 거리를 정해놓고 설치하는데
    # 만약에 C개보다 더 설치하면,
    # 거리를 조금 늘려야함
    # 
    # C개보다 덜 설치되면
    # 거리를 좁혀야함 
    houses.sort()

    answer=-float('inf')

    left=987654321
    right=max(houses)-min(houses)

    for idx in range(len(houses)-1):
        left=min(left,houses[idx+1]-houses[idx])

    # 5 3
    # 1 2 4 8 9

    def is_possible(mid):
        count=1

        prev=houses[0]

        for idx in range(1,len(houses)):
            dist=houses[idx]-prev

            if dist<mid:
                continue
            else:
                count+=1
                prev=houses[idx]


        # 오케 여기서 Count==C 줫더니 틀렸는데
        # 왜그럴까? 
        # 봐바 주어진 조건을 만족하게 
        # 그니까 모든 공유기 설치 지점끼리는
        # dist보다 크거나 같은 길이만큼 떨어져 있음
        # 다시말해서 dist는 closest router dist의 하한값인거임
        # 그니까 C개 이상설치했으면 그냥 몇개 빼버리면 되는거
        # C보다 10개 더설치되어있으면, 그냥 그 10개 더 빼버리자
        # 그래도 여전히 closest router dist는 유지됨
    
        if count>=C:
            return True
        else:
            return False

    
    while left<=right:

        mid=(left + right)//2

        # print(left, mid, right)

        if is_possible(mid):
            left=mid+1
            answer=max(answer,mid)
        else:
            right=mid-1
    
    return answer


print(sol())