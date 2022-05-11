from collections import deque

answer = 987654321


def solution(stones, k):

    # 한칸씩 건널때
    if k == 1:
        return min(stones)
    global answer

    max_len = len(stones)

    # O(N*k) 코드 : TLE
    # min_max_in_section=200000001

    # for start_idx in range(len(stones)-k+1):
    #     max_value=-1
    #     for i in range(start_idx,start_idx+k):
    #         max_value=max(max_value,stones[i])
    #     min_max_in_section=min(min_max_in_section,max_value)

    # answer=min_max_in_section
    # return answer

    # DFS 방식 : TLE
    # 한명이라도 오른쪽에 도착할수 있다면 answer+1
    # 한번이라도 도착못하면 바로 리턴

    # while True:
    #     is_possible=dfs(stones,k,max_len)

    #     if not is_possible:
    #         break

    # O(N*k) 수정버전

    # i = 0
    # while i < max_len - k:
    #     if stones[i] <= stones[i + 1]:
    #         i += 1
    #         continue
    #     else:
    #         is_ok = False
    #         max_in_selection = -1

    #         for step in range(1, k + 1):
    #             if stones[i] < stones[i + step]:
    #                 i = i + step
    #                 is_ok = True

    #                 break
    #             else:
    #                 max_in_selection = max(max_in_selection, stones[i + step])
    #         if not is_ok:
    #             answer = min(answer, max_in_selection)
    #             i += 1

    # return answer if answer != 987654321 else sorted(stones)[0]

    # 최소 시도는 한명이 건너는것,가장 많이 시도는 가장 큰 돌만큼 건너는 것
    left, right = 1, max(stones)
    answer = 1

    while left <= right:
        mid = (left + right) // 2

        can_pass = True

        consequtive_zero = 0
        for stone in stones:
            # stone이 mid보다 작으면 mid명이 건널수 없음
            # 0이 생기면 consequtive_zero의 값을 올림
            if stone < mid:
                consequtive_zero += 1
                # 0이 연속해서 k개 생기면 건널수 없음
                if consequtive_zero == k:
                    can_pass = False
                    break
            else:
                consequtive_zero = 0

        # 만약 충분히 건널수 있다면
        if can_pass:
            # answer을 더 큰값으로 교체
            answer = max(mid, answer)
            # 탐색을 오른쪽으로 옮김 -> 더 많은 니니즈들이 건널수 있도록 시도
            left = mid + 1
        # 건널수 없다면
        else:
            # 탐색을 왼쪽으로 옮김 -> 적은 수의 니니즈들이 건널수 있도록 시도
            right = mid - 1
    return answer


def dfs(stones, k, max_len):
    global answer
    stack = list()

    stack.append(-1)

    while len(stack) != 0:
        tos = stack.pop()
        for step in range(1, k + 1):
            # # 끝에 도달하면
            if tos + step >= max_len:
                answer += 1
                return True

            # 밟을수 있다면
            if stones[tos + step] != 0:
                stack.append(tos + step)
                stones[tos + step] -= 1
                break
    return False


if __name__ == "__main__":
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
