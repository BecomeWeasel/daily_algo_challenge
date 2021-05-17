from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

R, C = map(int, stdin.readline().split())


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


print(sol())