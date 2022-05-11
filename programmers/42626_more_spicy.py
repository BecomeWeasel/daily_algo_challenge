import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        # 이 방법이 min(scoville)<7 유지조건보다 빠름
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) < 1:
            return -1
        second = heapq.heappop(scoville)

        scoville.append(first + 2 * second)
        # heapq.heappush(scoville,first+2*second)
        answer += 1

    return answer
