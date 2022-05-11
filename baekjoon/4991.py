from sys import stdin
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol(w, h):

    board = []

    for _ in range(h):
        board.append(list(stdin.readline().strip()))

    # for r in board:
    #     print(r)

    dirty_count = 0

    init_y, init_x = -1, -1

    dirty = []

    for i in range(h):
        for j in range(w):
            if board[i][j] == "*":

                dirty.append((i, j))
                dirty_count += 1

            elif board[i][j] == "o":
                init_y, init_x = i, j

    q = deque()

    visit = [[[False for _ in range((1 << dirty_count) + 1)] for _ in range(20)] for _ in range(20)]

    visit[init_y][init_x][0] = True

    q.append((init_y, init_x, 0, 0))

    # 그 우주선탐사랑 좀 비슷한데
    # 얘가 가능한 이유는 O(2^10*20*20)=O(1024*400)

    while q:
        # 미친실수를했어요
        # y,x,bit,count=q.pop()

        y, x, bit, count = q.popleft()

        if bit == (1 << dirty_count) - 1:
            return count

        # if bit==(1<<dirty_c)

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if not (0 <= ny < h and 0 <= nx < w):
                continue

            if board[ny][nx] == "x":
                continue

            elif board[ny][nx] == "*":
                # 그 지역이 몇번째 치워야되는 장소인지
                dirty_number = dirty.index((ny, nx))
                #
                next_bit = bit | (1 << dirty_number)

                if visit[ny][nx][next_bit]:
                    continue

                visit[ny][nx][next_bit] = True
                q.append((ny, nx, next_bit, count + 1))
            else:

                if visit[ny][nx][bit]:
                    continue

                visit[ny][nx][bit] = True
                q.append((ny, nx, bit, count + 1))

    return -1


while True:
    w, h = map(int, stdin.readline().split())

    if w == 0:
        break

    print(sol(w, h))
