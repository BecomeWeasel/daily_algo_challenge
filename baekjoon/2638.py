from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M = map(int, stdin.readline().split())


def sol():
    board = [list(map(int, stdin.readline().split())) for _ in range(N)]

    time = 0

    while True:
        no_cheese = True

        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    no_cheese = False

        # 치즈가 모두 녹았다면 시간 반환
        if no_cheese:
            return time

        check = [[False for _ in range(M)] for _ in range(N)]
        # new_board = board[:]
        # cheese_queue = deque()

        # 외부 공기들을 전부 -1로 바꿈
        q = deque()
        q.append((0, 0))
        check[0][0] = True
        space_bfs(q, check, board)

        for i in range(N):
            for j in range(M):
                # 치즈발견했다면
                if board[i][j] == 1:
                    if is_melt(i, j, board):
                        board[i][j] = 0

        # 녹일수 있는 치즈는 다 녹임
        # while len(cheese_queue)!=0:
        #   y,x=cheese_queue.popleft()

        #   if is_melt(y,x,board):
        #     board[y][x]=0

        for i in range(N):
            for j in range(M):
                if board[i][j] == -1:
                    board[i][j] = 0

        time += 1

    return time


def space_bfs(q, check, board):

    while len(q) != 0:

        y, x = q.popleft()

        # 외부 공기는 -1로 표현
        board[y][x] = -1

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 새로운 외부공기를 만나면 q에 추가
            if 0 <= ny < N and 0 <= nx < M:
                if not check[ny][nx] and board[ny][nx] == 0:
                    q.append((ny, nx))
                    check[ny][nx] = True


def is_melt(y, x, board):

    outside_air = 0

    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]

        # 주변에 외부공기가 있다면
        # outside_air 1 증가
        if board[ny][nx] == -1:
            outside_air += 1

    # 사방에 외부공기가 2개이상이라면 녹아야함
    return True if outside_air >= 2 else False


print(sol())
