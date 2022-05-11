from sys import stdin
from collections import defaultdict, deque

R, C = map(int, stdin.readline().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():
    def print_board(board):
        for r in board:
            print("".join(r))

    board = [list(stdin.readline().rstrip()) for _ in range(R)]

    N = int(stdin.readline())
    cmd = list(map(int, stdin.readline().split()))

    for idx, cmd in enumerate(cmd):
        # 왼쪽에서 던질때
        if idx % 2 == 0:
            for x in range(C):
                if board[R - cmd][x] == "x":
                    board[R - cmd][x] = "."
                    break
        # 오른쪽에서 던질때
        else:
            for x in range(C - 1, -1, -1):
                if board[R - cmd][x] == "x":
                    board[R - cmd][x] = "."
                    break

        visit = [[False for _ in range(C)] for _ in range(R)]

        def bfs(q: deque, visit) -> list:
            nonlocal board
            minerals = []
            lowest_y = -1
            while q:
                y, x = q.popleft()
                lowest_y = max(lowest_y, y)
                minerals.append((y, x))

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]

                    if not (0 <= ny < R) or not (0 <= nx < C):
                        continue

                    if board[ny][nx] == "x" and not visit[ny][nx]:
                        visit[ny][nx] = True
                        q.append((ny, nx))

            # 가장 낮은 미네랄이 바닥에 닿아있으면 생략해도됨
            if lowest_y == R - 1:
                return []
            # 떠있으면 drop 대상이 됨
            else:
                return minerals

        dropped_cluster = []

        # 떨어질 클러스터 체크
        # 클러스터에서 가장 낮은 y좌표가 R-1이 아니라면 떠있다고 간주 -> heapq 사용가능

        keep_search = True

        for i in range(R):
            if not keep_search:
                break
            for j in range(C):
                if board[i][j] == "x" and not visit[i][j]:
                    visit[i][j] = True
                    q = deque()
                    q.append((i, j))

                    mineral = sorted(bfs(q, visit), key=lambda pos: (-pos[0], pos[1]))

                    # 땅바닥에 닿아있는 클러스터면 검사할 필요 없음
                    if len(mineral) == 0:
                        continue

                    # 땅바닥에 닿아있는 클러스터 하나를 찾으면
                    # 다음 클러스터는 검색할 필요가 없음
                    # 어차피 하나의 클러스터만 떨어지니
                    keep_search = False

                    lowest_pos = mineral[0][0]

                    if lowest_pos != R - 1:
                        # 어차피 드롭은 1개뿐
                        dropped_cluster = mineral

        # # 떨어질것이 없다면 돌을 계속 던지면 됨
        # if len(dropped_cluster) == 0:
        #     continue

        # 떨어질 높이를 구해야함
        # 미네랄 클러스터 각각의 x에 대해서 가장 낮은 y를 구함
        # 각각의 y에 대해서 board에서 거리를 구함 (얼마나 떠 있는지)
        y_dict = defaultdict(lambda: -1)
        for pos in dropped_cluster:
            y, x = pos
            y_dict[x] = max(y_dict[x], y)

        min_drop = R

        for mineral_x in y_dict.keys():

            dropped_mineral_lowest_y = y_dict[mineral_x]

            max_y = R
            for y in range(R - 1, dropped_mineral_lowest_y, -1):
                if board[y][mineral_x] == "x":
                    max_y = min(max_y, y)

            min_drop = min(max_y - dropped_mineral_lowest_y - 1, min_drop)

        # 이제 클러스터를 min_drop 만큼 아래로 내려야함
        for pos in dropped_cluster:
            y, x = pos
            board[y][x] = "."
            board[y + min_drop][x] = "x"

    print_board(board)


sol()
