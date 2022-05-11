def solution(citations):
    answer = 0

    left, right = 0, max(citations)

    # 입력이 [100] 인 경우에 left==right==100인데 답은 1이니 탐색 범위 밖
    # left,right=min(citations),max(citations)

    while left <= right:

        mid = (left + right) // 2

        count = 0

        count = sum(1 for x in citations if x >= mid)

        if count >= mid:
            left = mid + 1
            answer = max(answer, mid)
        else:
            right = mid - 1

    return answer
