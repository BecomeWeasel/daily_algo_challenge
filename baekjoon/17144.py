from sys import stdin
from collections import deque

# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C, T = map(int, stdin.readline().split())


def sol():
    board = [list(map(int, stdin.readline().split())) for _ in range(R)]

    purifier_x, purifier_y1, purifier_y2 = -1, -1, -1

    # y1이 공기청정기의 윗부분
    # 공기청정기는 (x,y1),(x,y2)에 위치
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                purifier_x = j
                if purifier_y1 == -1:
                    purifier_y1 = i
                else:
                    purifier_y2 = i

    # T초 동안
    for t in range(T):
        moved_dust_board = [row[:] for row in board]

        # 미세먼지 퍼트리기
        for i in range(R):
            for j in range(C):
                # 미세먼지가 쌓여있는 구역이면
                if board[i][j] != 0 and board[i][j] != -1:
                    num_possible_grid, possible_grid = get_possible_spread(board, i, j)

                    spread_amount = int(board[i][j] / 5)
                    # (j,i)에 남아있는 잔여량
                    moved_dust_board[i][j] -= spread_amount * num_possible_grid

                    for ny, nx in possible_grid:
                        moved_dust_board[ny][nx] += int(board[i][j] / 5)

        board = [row[:] for row in moved_dust_board]

        # 위 반시계방향 순환

        # 순환 시작점,초기 방향은 동쪽
        pos_y, pos_x, direction = 0, 0, 1

        # 공기청정기가 오른쪽끝에 붙어있다면
        if purifier_x == C - 1:
            pos_y, pos_x = purifier_y1 - 1, purifier_x
            direction = 0
        else:
            pos_y, pos_x = purifier_y1, purifier_x + 1

        origin_dust_values = []
        origin_dust_pos = []

        while True:
            origin_dust_pos.append((pos_y, pos_x))
            origin_dust_values.append(board[pos_y][pos_x])

            ny, nx = pos_y + dy[direction], pos_x + dx[direction]

            # 가다가 방향이 바뀌어야 한다면(벽에 부딪힌다면)
            if ny < 0 or ny == R or nx < 0 or nx == C:
                direction = (direction + 3) % 4
                ny, nx = pos_y + dy[direction], pos_x + dx[direction]

            if board[ny][nx] == -1:
                break
            pos_y, pos_x = ny, nx

        # 깨끗한 공기 하나 앞에 넣어주고(공기청정기에서 나온 깨끗한 공기)
        # 뒤 미세먼지 하나 삭제(공기청정기로 빨아들어가는 먼지)
        origin_dust_values = origin_dust_values[: len(origin_dust_values) - 1]
        origin_dust_values.insert(0, 0)

        # 한칸씩 다시 미세먼지 옮겨적기
        for idx, pos in enumerate(origin_dust_pos):
            board[pos[0]][pos[1]] = origin_dust_values[idx]

        # 아래 시계방향 순환

        # 순환 시작점,초기 방향은 동쪽
        pos_y, pos_x, direction = 0, 0, 1

        # 공기청정기가 오른쪽끝에 붙어있다면
        if purifier_x == C - 1:
            pos_y, pos_x = purifier_y2 + 1, purifier_x
            direction = 0
        else:
            pos_y, pos_x = purifier_y2, purifier_x + 1

        origin_dust_values = []
        origin_dust_pos = []

        while True:
            origin_dust_pos.append((pos_y, pos_x))
            origin_dust_values.append(board[pos_y][pos_x])

            ny, nx = pos_y + dy[direction], pos_x + dx[direction]

            # 가다가 방향이 바뀌어야 한다면(벽에 부딪힌다면)
            if ny < 0 or ny == R or nx < 0 or nx == C:
                direction = (direction + 1) % 4
                ny, nx = pos_y + dy[direction], pos_x + dx[direction]

            if board[ny][nx] == -1:
                break
            pos_y, pos_x = ny, nx

        # 깨끗한 공기 하나 앞에 넣어주고(공기청정기에서 나온 깨끗한 공기)
        # 뒤 미세먼지 하나 삭제(공기청정기로 빨아들어가는 먼지)
        origin_dust_values = origin_dust_values[: len(origin_dust_values) - 1]
        origin_dust_values.insert(0, 0)

        # 한칸씩 다시 미세먼지 옮겨적기
        for idx, pos in enumerate(origin_dust_pos):
            board[pos[0]][pos[1]] = origin_dust_values[idx]

    return sum_dust(board)


def get_possible_spread(board, y, x):
    possible_grid = list()
    count = 0
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] != -1:
            count += 1
            possible_grid.append((ny, nx))

    return count, possible_grid


def sum_dust(board):

    # 현재 지도상의 모든 미세먼지 양 출력
    # 단 공기청정기 -1이 2개 있으므로 +2를 해줘야함
    amount = sum(sum(board[i]) for i in range(R)) + 2

    return amount


print(sol())
