from sys import stdin
from bisect import bisect_left, bisect_right


def sol():
    N, H = map(int, stdin.readline().split())

    # 이 높이부터 위로 가면 생존
    bottom = list()

    # 이 높이부터 아래로 가면 생존
    top = list()

    for i in range(N):
        h = int(stdin.readline())
        # 천장에
        if i % 2 == 1:
            top.append(H - h)
        else:
            bottom.append(h)

    top.sort()
    bottom.sort()

    min_answer = float("inf")
    count = 0

    for h in range(1, H + 1):
        top_collision = bisect_left(top, h)
        bottom_collision = N // 2 - bisect_left(bottom, h)

        if top_collision + bottom_collision <= min_answer:
            if top_collision + bottom_collision == min_answer:
                count += 1

            else:
                min_answer = top_collision + bottom_collision
                count = 1

    print(min_answer, count)


sol()
