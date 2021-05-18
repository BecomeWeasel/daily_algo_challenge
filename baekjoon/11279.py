import heapq
from sys import stdin


def sol():
    N = int(stdin.readline())

    max_heap = []
    for _ in range(N):
        command = int(stdin.readline())

        if command == 0:
            if len(max_heap) == 0:
                print(0)
            else:
                # heappop은 pop을 먼저 해주고 heapify를 수행함
                # 그렇기 때문에 max or min-heap이 이루어지지 않은상태에서
                # heappop을 하면 max or min value를 보장할 수 없음
                print(heapq.heappop(max_heap)[1])

        else:
            heapq.heappush(max_heap, (-command, command))


sol()
