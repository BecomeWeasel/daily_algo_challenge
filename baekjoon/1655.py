from sys import stdin
import heapq as hq

N = int(stdin.readline())


def add_number(number, max_heap, min_heap):

    if len(max_heap) == 0 or number < max_heap[0][1]:
        hq.heappush(max_heap, (-number, number))
    else:
        hq.heappush(min_heap, (number, number))


def rebalance(max_heap, min_heap):
    bigger = max_heap if len(max_heap) > len(min_heap) else min_heap
    smaller = min_heap if len(max_heap) > len(min_heap) else max_heap

    if len(bigger) - len(smaller) >= 2:
        # value=hq.heappop(bigger)[1]
        value = bigger[0][1]
        del bigger[0]

        if smaller == max_heap:
            # smaller.append((-value,value))
            hq.heappush(smaller, (-value, value))
        else:
            # smaller.append((value,value))
            hq.heappush(smaller, (value, value))


def get_median(max_heap, min_heap):
    bigger = max_heap if len(max_heap) > len(min_heap) else min_heap
    smaller = min_heap if len(max_heap) > len(min_heap) else max_heap

    # 개수가 같으면 (들어온것이 짝수개이면) 작은것이 중간값
    if len(bigger) == len(smaller):
        return smaller[0][1]
    else:
        return bigger[0][1]


def sol():
    # max_heap : max heap
    # min_heap : min heap
    max_heap, min_heap = list(), list()
    for _ in range(N):
        num = int(stdin.readline())
        # add_number(num, max_heap, min_heap)
        # rebalance(max_heap, min_heap)
        # print(get_median(max_heap, min_heap))

        if len(max_heap) != len(min_heap):
            hq.heappush(min_heap, (num, num))
        else:
            hq.heappush(max_heap, (-num, num))

        if not len(max_heap) == 0 and not len(min_heap) == 0 and max_heap[0][1] > min_heap[0][1]:
            max_heap_v, min_heap_v = hq.heappop(max_heap)[1], hq.heappop(min_heap)[1]

            hq.heappush(min_heap, (max_heap_v, max_heap_v))
            hq.heappush(max_heap, (-min_heap_v, min_heap_v))

        print(max_heap[0][1])


sol()
