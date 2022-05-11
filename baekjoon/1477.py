### AC를 받음
from sys import stdin


def sol():
    N, M, L = map(int, stdin.readline().split())

    stops = list(map(int, stdin.readline().split()))
    stops.append(0)
    stops.append(L)
    stops.sort()

    l, r = 0, L - 1

    for i in range(N + 1):
        d = stops[i + 1] - stops[i]
        l = min(l, d)
        r = max(r, d)

    min_answer = float("inf")
    while l <= r:
        mid = (r + l) // 2
        count = 0

        for i in range(N + 1):
            count += (stops[i + 1] - stops[i] - 1) // mid

        if count > M:
            l = mid + 1
        else:
            min_answer = min(mid, min_answer)
            r = mid - 1
        """ 
        극단적으로 휴게소를 1만큼의 간격마다 세운다면 count는 M보다 큰 조건을 만족하는데
        그럴때에도 최솟값이라고 할수는 없음

        반대로 count가 M개보다 적다면 더 쪼갤 공간이 있으니 길이를 줄여야함
        3개만큼 부족하면 그냥 아무데나 배치해도 mid값을 지킬수있음, 안쓴 휴게소가 남았다고 생각하면 됨
        if count >= M:
            min_answer = min(mid, min_answer)
            l = mid + 1
        else:
            r = mid - 1
        """
    return min_answer


print(sol())
