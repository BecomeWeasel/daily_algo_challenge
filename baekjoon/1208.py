from collections import defaultdict
from sys import stdin

N, S = map(int, stdin.readline().split())


def sol():
    global N, S
    count = 0
    numbers = list(map(int, stdin.readline().split()))

    # set만쓰면 다 표현못함 중복되는거 ㅇㅇ
    # first_half=set()
    # second_half=set()

    first_half = defaultdict(int)
    second_half = defaultdict(int)

    # 걍 two sum의 응용판 버전임

    # two sum이 뭐임 결국에 원소두개비굔데
    # 얜 그냥 원소를 aggregation 해서 보겟다는거

    def dfs(step, idx, total, limit):
        nonlocal count, numbers
        if step == limit:
            first_half[total] += 1
            return

        dfs(step + 1, idx + 1, total + numbers[idx + 1], limit)
        dfs(step + 1, idx + 1, total, limit)

    def dfs2(step, idx, total, limit):
        nonlocal count, numbers
        if step == limit:
            second_half[total] += 1
            return

        dfs2(step + 1, idx + 1, total + numbers[idx + 1], limit)
        dfs2(step + 1, idx + 1, total, limit)

    if N == 1:
        if numbers[0] == S:
            return 1
    else:
        left = N // 2
        dfs(1, 0, numbers[0], left)
        dfs(1, 0, 0, left)

        dfs2(left + 1, left, numbers[left], N)
        dfs2(left + 1, left, 0, N)

    # 만약에 f_k만큼의 값을 S에서 뺀 S-f_k가 존재하면,
    # f_k를 만드는 경우의 수 x S-f_k를 만드는 경우의 수가 S를 만드는 횟수에 추가되어야함.
    # 왜 곱하냐면, f_k를 만드는 방법이 3가지고 S-f_k를 만드는 방법이 2가지면
    # 양쪽에서 하나씩 고르는 전형적인 문제니까..
    for f_k in first_half.keys():
        if S - f_k in second_half.keys():
            count += (first_half.get(f_k)) * (second_half.get(S - f_k))

    # 만약에 0이면, dfs 중에서 아예 아무것도 선택안한것도 잇음
    return count if S != 0 else count - 1


print(sol())
