from sys import stdin
from itertools import combinations, product

N, M = map(int, stdin.readline().split())


def sol():
    board = []

    class CCTV:
        def __init__(self, type, y, x):
            self.type = type
            self.y = y
            self.x = x
            self.cover = []

    cctv_count = 0
    wall_count = 0

    for _ in range(N):
        board.append(list(stdin.readline().split()))
    cctv_list = list()
    for i in range(N):
        for j in range(M):
            if board[i][j] in ["1", "2", "3", "4", "5"]:
                cctv_list.append(CCTV(board[i][j], i, j))
                cctv_count += 1
            elif board[i][j] == "6":
                wall_count += 1

    def cctv_traversal(tv: CCTV):
        def down_traversal(y, x) -> list:
            global N, M
            nonlocal board
            tmp = list()
            for i in range(y + 1, N):
                if not (0 <= i < N):
                    break
                if board[i][x] == "6":
                    break
                elif board[i][x] == "0":
                    tmp.append([i, x])
            return tmp

        def up_traversal(y, x) -> list:
            global N, M
            nonlocal board
            tmp = list()
            for i in range(y - 1, -1, -1):
                if not (0 <= i < N):
                    break
                if board[i][x] == "6":
                    break
                elif board[i][x] == "0":
                    tmp.append([i, x])

            return tmp

        def left_traversal(y, x) -> list:
            global N, M
            nonlocal board

            tmp = list()

            for i in range(x - 1, -1, -1):
                if not (0 <= i < M):
                    break
                if board[y][i] == "6":
                    break
                elif board[y][i] == "0":
                    tmp.append([y, i])

            return tmp

        def right_traversal(y, x) -> list:
            global N, M
            nonlocal board

            tmp = list()
            for i in range(x + 1, M):
                if not (0 <= i < M):
                    break
                if board[y][i] == "6":
                    break
                elif board[y][i] == "0":
                    tmp.append([y, i])

            return tmp

        global N, M
        nonlocal board
        if tv.type == "1":
            tv.cover.append(up_traversal(tv.y, tv.x))
            tv.cover.append(right_traversal(tv.y, tv.x))
            tv.cover.append(down_traversal(tv.y, tv.x))
            tv.cover.append(left_traversal(tv.y, tv.x))
        elif tv.type == "2":
            # 상하 영역 추가
            tv.cover.append(down_traversal(tv.y, tv.x) + up_traversal(tv.y, tv.x))
            # 좌우 영역 추가
            tv.cover.append(left_traversal(tv.y, tv.x) + right_traversal(tv.y, tv.x))

        elif tv.type == "3":
            # 상,우 영역추가
            tv.cover.append(down_traversal(tv.y, tv.x) + right_traversal(tv.y, tv.x))
            # 우,하 영역추가
            tv.cover.append(right_traversal(tv.y, tv.x) + up_traversal(tv.y, tv.x))
            # 좌,하 영역추가
            tv.cover.append(up_traversal(tv.y, tv.x) + left_traversal(tv.y, tv.x))
            # 좌,상 영역추가
            tv.cover.append(left_traversal(tv.y, tv.x) + down_traversal(tv.y, tv.x))
        elif tv.type == "4":
            # 아래 제외
            tv.cover.append(
                up_traversal(tv.y, tv.x) + left_traversal(tv.y, tv.x) + right_traversal(tv.y, tv.x)
            )
            # 좌측 제외
            tv.cover.append(
                up_traversal(tv.y, tv.x) + right_traversal(tv.y, tv.x) + down_traversal(tv.y, tv.x)
            )
            # 우측 제외
            tv.cover.append(
                up_traversal(tv.y, tv.x) + down_traversal(tv.y, tv.x) + left_traversal(tv.y, tv.x)
            )
            # 상단 제외
            tv.cover.append(
                down_traversal(tv.y, tv.x)
                + right_traversal(tv.y, tv.x)
                + left_traversal(tv.y, tv.x)
            )
            # pass
        elif tv.type == "5":
            tv.cover.append(
                down_traversal(tv.y, tv.x)
                + right_traversal(tv.y, tv.x)
                + up_traversal(tv.y, tv.x)
                + left_traversal(tv.y, tv.x)
            )

    coverage_list = list()

    for cctv in cctv_list:
        cctv_traversal(cctv)
        coverage_list.append(cctv.cover)

    max_cover = -1
    for combi in list(product(*coverage_list)):
        max_cover = max(len(set(map(tuple, list(sum(combi, []))))), max_cover)

    return N * M - max_cover - cctv_count - wall_count


print(sol())
