from sys import stdin
from collections import deque
from math import sqrt, ceil

n, k = map(int, stdin.readline().split())
end_y, end_x = 10000, 10000


def sol():
    nodes = []
    for i in range(n):
        x, y = map(int, stdin.readline().split())
        nodes.append((y, x))
    nodes.append((end_y, end_x))

    # 목적지까지 가는 최대 엣지의 개수를 K개이하로 만들어야함.
    # K값이 엄청 낮다고 해보자 . 예를 들어 K=0
    # 그럼 S->T 까지 한번에 가야함

    # 이러면 최소 연료통의 크기가 커짐

    # 반대로 K값을 엄청 키워보자.
    # 그러면 조금가고 멈추고 , 조금가고 멈추고 반복임
    # 최소 연료통의 크기도 낮아짐

    # 결국에 K와 최소 연료통의 크기는 반비례하는거 -> 결정문제라고 보기는 조금 애매한데..
    # 왜냐면 모든 경우에서 다 도착은 하거든
    # 그럼 반대로 최소연료통 용량 정해놓고 K안에 도착하나를 볼까

    # 최소 연료통 용량의 최대값은 k=0일때 S->T 바로가니까 sqrt(10000^2+10000^2)=14142 니까 14150임
    # 최소는 음................................................................
    # 최소는 0,0에서 10000,10000까지 가는 대각선 루트에서 1000개 있을때 얘기니까
    # 14142를 1000으로 나눈 값인 14에서 올림해서 20

    # 3<=n<=1000 0<x,y<10000
    # 엣지는 n^2개쯤..

    # 오케이 일단 풀었는데,
    # 궁금한점 visit을 naive하게 구성했더니 오히려 맞아
    # 왜그런걸까

    # 생각해보면, 특정 지점 X가 True로 바뀌었으면 그 지점에는 mid 값을 가지고
    # X를 방문할 수 있었단 거임 . 그러니까 다시 X를 중간지점으로 삼고 도착지로 삼는 루트를 다시 계산해줄 필요가 없음
    # TF로 두는게 더 효율적인 방식임

    # 만약 그 지점 X가 False 라고 해보자. 그럼 다른지점 Y에서 X까지 mid 안에 가는건 실패했지만
    # 또 다른지점 Z에서 X까지 mid 안에 가는 루트가 있을순 있는거임
    def is_possible(mid):
        global k
        # visit = [float('inf') for _ in range(n + 1)]
        visit = [False for _ in range(n + 1)]

        # visit.add((0, 0))

        q = deque()

        q.append((0, 0, 0))

        while q:
            y, x, count = q.popleft()

            if y == end_y and x == end_x:
                return True

            if count > k:
                continue

            for idx, node in enumerate(nodes):
                ny, nx = node
                dist = ceil(sqrt(abs(y - ny) ** 2 + abs(x - nx) ** 2))

                fuel = int((dist + 9) / 10 * 10) // 10

                if fuel > mid:
                    continue

                # if visit[idx] < fuel:
                if visit[idx]:
                    continue

                q.append((ny, nx, count + 1))
                # visit[idx] = fuel
                visit[idx] = True
        return False

    left, right = 20, 14150

    answer = float("inf")

    while left <= right:
        mid = (left + right) // 2

        if is_possible(mid):
            answer = min(answer, mid)

            right = mid - 1
        else:
            left = mid + 1

    return answer


print(sol())
