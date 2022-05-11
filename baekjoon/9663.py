from sys import stdin

N = int(stdin.readline())
cnt = int(0)

vertical_check = set()
# \ 대각선 체크
right_top_to_left_bottom_check = set()
# / 대각선 체크
left_top_to_right_bottom_check = set()


def sol():
    global cnt

    def dfs(k):
        global N, cnt
        if k == N:
            cnt += 1

        for i in range(1, N + 1):
            if (
                (i in vertical_check)
                or (i + k + 1 in right_top_to_left_bottom_check)
                or (k + 1 - i in left_top_to_right_bottom_check)
            ):
                continue
            vertical_check.add(i)
            right_top_to_left_bottom_check.add(i + k + 1)
            left_top_to_right_bottom_check.add(k + 1 - i)
            dfs(k + 1)
            right_top_to_left_bottom_check.remove(i + k + 1)
            left_top_to_right_bottom_check.remove(k + 1 - i)
            vertical_check.remove(i)

    for i in range(1, N + 1):
        vertical_check.add(i)
        right_top_to_left_bottom_check.add(i + 1)
        left_top_to_right_bottom_check.add(1 - i)
        # 1번째 row,i번째 col에 퀸 놓기
        dfs(1)
        right_top_to_left_bottom_check.remove(i + 1)
        left_top_to_right_bottom_check.remove(1 - i)
        vertical_check.remove(i)

    return cnt


print(sol())
