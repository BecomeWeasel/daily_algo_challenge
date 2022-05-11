from sys import stdin


def ans(param_num_list, N):
    param_num_list.sort()

    answer_list = [0 for _ in range(N)]

    if N % 2 == 0:
        mid = int(N / 2)
        answer_list[mid] = param_num_list[N - 1]
        remain_pos = N - 2
        left = right = mid
        for i in range(1, int(N / 2)):
            left -= 1
            right += 1
            answer_list[left] = param_num_list[remain_pos]
            remain_pos -= 1
            answer_list[right] = param_num_list[remain_pos]
            remain_pos -= 1
        answer_list[0] = param_num_list[0]

    else:
        mid = int((N - 1) / 2)
        # 중앙에 제일 큰 수 배치
        answer_list[mid] = param_num_list[N - 1]
        remain_pos = N - 2
        left = right = mid
        for i in range(1, int((N - 1) / 2) + 1):
            left -= 1
            right += 1
            answer_list[left] = param_num_list[remain_pos]
            remain_pos -= 1
            answer_list[right] = param_num_list[remain_pos]
            remain_pos -= 1

    max_diff = 0
    for i in range(N):
        max_diff = max(max_diff, int(abs(answer_list[i % N] - answer_list[(i + 1) % N])))

    return max_diff


T = int(stdin.readline())
for k in range(T):
    N = int(stdin.readline())
    num_list = list(map(int, stdin.readline().split()))
    print(ans(num_list, N))
