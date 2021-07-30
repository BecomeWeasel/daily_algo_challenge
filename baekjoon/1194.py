from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():

    board = []

    for _ in range(N):
        board.append(list(stdin.readline().rstrip()))

    # print(board)

    visit = set()

    posy, posx = -1, -1

    for i in range(N):
        for j in range(M):
            if board[i][j] == '0':
                posy, posx = i, j

    q = deque()
    q.append((posy, posx, 0, 0))
    visit.add((posy, posx, 0))

    def OOB(y, x):
        if not (0 <= y < N) or not (0 <= x < M):
            return True
        return False

    while q:
        y, x, count, visit_bit = q.popleft()

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if OOB(ny, nx):
                continue

            if (ny, nx, visit_bit) in visit or board[ny][nx] == '#':
                continue

            if board[ny][nx] == '1':
                return count + 1
            elif board[ny][nx] in {'a', 'b', 'c', 'd', 'e', 'f'}:
                key_num = ord(board[ny][nx]) - 97

                new_visit_bit = visit_bit | (1 << key_num)

                visit.add((ny, nx, new_visit_bit))
                q.append((ny, nx, count + 1, new_visit_bit))
            elif board[ny][nx] in {'A', 'B', 'C', 'D', 'E', 'F'}:
                door_num = ord(board[ny][nx]) - 65

                # 열쇠가 있음
                if visit_bit & (1 << door_num) > 0:
                    visit.add((ny, nx, visit_bit))
                    q.append((ny, nx, count + 1, visit_bit))
            elif board[ny][nx] == '.' or board[ny][nx] == '0':
                visit.add((ny, nx, visit_bit))
                q.append((ny, nx, count + 1, visit_bit))

    return -1


print(sol())