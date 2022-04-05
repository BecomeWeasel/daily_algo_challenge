from os import remove
from sys import stdin
from unittest import result


def sol():
    N = int(stdin.readline())
    M = int(stdin.readline())

    bus = []

    for i in range(1, M + 1):
        a, b = map(int, stdin.readline().split())
        bus.append((i, a, b))

    is_remove = [False for _ in range(M + 1)]

    # N 제한이 3에서부터 10억까지
    # M은 2에서부터 50만까지
    # [a,b] 인데 a부터 b까지는 정방향
    # b부터 a까지는 역방향

    # 만약 모든 버스가 a<b라고 해보자
    # 그럼 0~N까지 일직선 상에 노선을 표시할 수 있음.

    # 그랬을때 예시를 보자
    # [0,4] , [2,6] [5,0] [7,9], [9,4]
    # 에서 3,5제외하고 수직선상에 나타내면

    # 0 1 2 3 4 5 6 7 8 9
    # <------->             1
    #     <------->         2
    #               <---->  4

    # 이제 여기에 오버래핑하는 구간 추가해보자.

    # 일단 [1,6] 추가 [4,9] 추가
    # 0 1 2 3 4 5 6 7 8 9
    # <------->             1
    #     <------->         2
    #               <---->  4
    #   <--------->         A
    #         <---------->  B

    # 출발 작은 순으로 정렬하면
    # 0 1 2 3 4 5 6 7 8 9
    # <------->             1
    #   <--------->         A
    #     <------->         2
    #         <---------->  B
    #               <---->  4

    # 이걸보면, 출발이 가장 작은
    # 1은 누구에게도 포함되지 A를 포함할 가능성이 있음
    # 1의 끝과 A의 끝을 비교하면 아님

    # A는 2번보다 출발지점이 빠르고 도착지점은 동일함
    # 따라서 포함함

    # 임의의 정렬된 버스노선 X,Y에서
    # X출발=Y출발이면, 도착지점 비교 , Y가 더 크다면 Y는 X에 포함되지 않음
    # 만약 다르다면 X 도착>=Y도착이면 무조건 포함
    # 출발지점이 다른데 X 도착<Y도착이면 X는 이제 더 이상 아무것도 포함하지 못함

    # 이러면 M번이면 될거같은데

    # 만약 출발지점이 다른데 X도착 Y 도착이면 , Y에서부터 탐색시작하면 됨
    # X와 Y사이에 있는 버스노선은 어차피 X가 무조건 포함하고, Y를 포함시키지 못함

    # <-------->     : X
    # <----->        : sub 1
    # <-->           : sub 2
    #   <---->       : sub 3
    #   <--------->  : Y

    # 만약 둘이 출발지점이 같다면, 길이가 긴건 무조건 짧은걸 포함함
    # 동일한 버스노선은 없기 때문에

    remove_bus = set()

    # 출발지점이 작은것부터, 지점이 같다면 길이가 긴게 먼저

    bus.sort(key=lambda x: (x[1], -(x[2] - x[1])))

    cursor = 0
    next_cursor = cursor + 1

    # print(bus)

    # 끝에서 두번째 버스노선까지 검사
    while cursor < M - 1 and next_cursor < M:

        x, start, end = bus[cursor]

        y, next_start, next_end = bus[next_cursor]

        # print(f"버스 번호 :{x} : {start} -> {end}")
        # print(f"버스 번호 :{y} : {next_start} -> {next_end}")
        # print("----")
        if start == next_start:
            next_cursor += 1
            is_remove[y] = True
            # print(f"출발지점 같은 버스 {start}->{end} 가 {next_start}->{next_end}를 포함")
        else:
            if end >= next_end:
                next_cursor += 1
                is_remove[y] = True
                # print(f"긴 구간 포함 버스 {start}->{end} 가 {next_start}->{next_end}를 포함")
            else:
                cursor = next_cursor
                next_cursor = cursor + 1

    # print(remove_bus)
    ret = [str(i) for i in range(1, M + 1) if not is_remove[i]]


    # 오케 이러면 테케 일부는 뿌쉇는데
    # 나머지 처리를 어떻게하지
    # 결국 문제는 a>b 노선인데
    # a>b 노선 vs a<b 비교?
    # a>b 노선 둘은 그냥 노선 두배로 늘여서 보면됨

    # a > b이면 대충 [4,0] 이런거일텐데 
    # 그냥 4,5,6,7,8,9,0 이렇게 간다고 보지말고
    # 4,5,6,7,8,9,10, 라고 생각해보자. 
    # 다른 노선을 [2,1]이라고 하면
    # 얘도 그냥 2,3,4,5,6,7,8,9,0,1 이라고 하지말고
    # 2,3,4,5,6,7,8,9,10,11 이라고 보는거임

    # 왜냐면 순환지점 도는순간 귀찮아지니까

    # 그니까 end 지점에 

    # 0 1 2 3 4 5 6 7 8 9
    # >        ----------
    # --> ---------------  

    # 이거를 그냥 반대로 두배 만들어버리는거 , 어차피 길이는 중요한게 아님  노선안에서 포함여부만 중요한거
    # 이러면 걍 이거는 아까풀었던거처럼 풀면됨
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
    #         ------------->
    #     -------------------->

    # 그럼 a>b 노선하고 a<b 노선은 어케풀까
    # [0,4] , [9,4]
    # 0 1 2 3 4 5 6 7 8 9
    # >         ---------  
    # -------->         -


    return ' '.join(ret)


print(sol())
