def solution(n, times):

    # 어처구니 없는 long long 이슈
    # 최대 시간이 987654321보다 클때
    # min(answer,mid)를 사용하기때문에 정답이 갱신되지 않음
    # answer=987654321

    answer = 987654321987654321

    # left, right = 1, (len(times) + 1) * max(times)
    left, right = 1, n * max(times)

    while left <= right:
        mid = (left + right) // 2

        done_num = 0

        done_num = sum(mid // time for time in times)

        # 원하는 만큼 수행했거나 더 수행했으므로
        # 시간을 줄여봐도됨
        if done_num >= n:
            answer = min(answer, mid)
            right = mid - 1
        # 원하는 만큼 수행하지 못했다면 시간을 늘여야함
        elif done_num < n:
            left = mid + 1

    return answer


if __name__ == "__main__":
    print(solution(6, [7, 10]))
