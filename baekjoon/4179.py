from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

R, C = map(int, stdin.readline().split())
""" 
# 불과 지훈이 동시에 움직이는 방식
def is_border(y, x):
    global R, C
    if y == 0 or x == 0 or y == R-1 or x == C-1:
        return True
    return False


def sol():
    board = []

    for _ in range(R):
        board.append(list(stdin.readline().rstrip()))

    visit = [[False for _ in range(C)] for _ in range(R)]
    move = deque()
    fire = deque()

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'J':
                move.append((i, j))
                visit[i][j] = True
            elif board[i][j] == 'F':
                fire.append((i, j))

    time = 0

    while True:
        new_move = deque()
        while len(move) != 0:
            y, x = move.pop()

            # 움직인 자리에 불이 붙었으면
            if board[y][x] == 'F':
                continue

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]

                # 맵을 벗어나면 탈출에 성공한것
                if ny < 0 or ny == R or nx < 0 or nx == C:
                    return time+1


                if not visit[ny][nx] and board[ny][nx] == '.':
                    new_move.append((ny, nx))
                    visit[ny][nx] = True
        
        if len(new_move)==0:
            return 'IMPOSSIBLE'

        new_fire = deque()
        while len(fire) != 0:

            y, x = fire.pop()

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]

                if 0 <= ny < R and 0 <= nx < C and not (board[ny][nx] == 'F' or
                                                        board[ny][nx] == '#'):
                    board[ny][nx] = 'F'
                    new_fire.append((ny, nx))

        while len(new_fire) != 0:
            ny, nx = new_fire.pop()
            fire.append((ny, nx))

        while len(new_move) != 0:
            ny, nx = new_move.pop()
            move.append((ny, nx))
        time += 1
"""


def sol():
    fire_spread = [[float("inf") for _ in range(C)] for _ in range(R)]
    board = []

    for _ in range(R):
        board.append(list(stdin.readline().rstrip()))

    f_queue = deque()

    start_y, start_x = 0, 0

    for i in range(R):
        for j in range(C):
            if board[i][j] == "F":
                f_queue.append((i, j, 0))
                fire_spread[i][j] = 0
            elif board[i][j] == "J":
                start_y, start_x = i, j

    # 처음부터 가장자리면 1초 뒤에 바로 탈출
    if start_y == 0 or start_y == R - 1 or start_x == 0 or start_x == C - 1:
        return 1

    def fire_bfs(q):
        nonlocal board, fire_spread
        while q:
            y, x, time = q.popleft()

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]

                if not (0 <= ny < R and 0 <= nx < C):
                    continue

                # 불이 퍼질수 없거나 이미 계산이 되었다면
                if board[ny][nx] == "#" or fire_spread[ny][nx] != float("inf"):
                    continue

                fire_spread[ny][nx] = time + 1
                q.append((ny, nx, time + 1))

    fire_bfs(f_queue)

    move_q = deque()
    move_q.append((start_y, start_x, 0))

    dist = [[-1 for _ in range(C)] for _ in range(R)]
    dist[start_y][start_x] = 0

    while move_q:

        y, x, time = move_q.popleft()

        # 불이 붙은곳에 있다면
        if time >= fire_spread[y][x]:
            continue

        # print(y,x,time)
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            # 탈출 성공
            if not (0 <= ny < R and 0 <= nx < C):
                return dist[y][x] + 1

            # 벽이거나
            if board[ny][nx] == "#":
                continue

            # 이미 방문
            if dist[ny][nx] >= 0:
                continue

            dist[ny][nx] = dist[y][x] + 1
            move_q.append((ny, nx, dist[ny][nx]))

    return "IMPOSSIBLE"


print(sol())
