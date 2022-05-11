from sys import stdin
from collections import deque

N = 3

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def sol():
    board = []
    for _ in range(3):
        board.append(list(map(int, stdin.readline().split())))

    pos_y, pos_x = 0, 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                pos_y, pos_x = i, j

    def serialize(board):
        ret = ""
        for num in sum(board, []):
            ret += str(num)
        return int(ret)

    def deserialize(s):
        s = str(s)

        tmp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # 시작이 0으로 시작하면 직렬화된 배열이 8자리
        if len(s) == 8:
            s = "0" + s
        for idx, num in enumerate(s):
            i = idx
            y = i // 3
            x = i % 3

            tmp[y][x] = int(num)

        return tmp

    def bound_safe(y, x):
        if not (0 <= y < N) or not (0 <= x < N):
            return False
        return True

    answer = 123456780

    # print(deserialize(answer))

    q = deque()
    visit = set()
    q.append((pos_y, pos_x, serialize(board), 0))

    while q:
        y, x, serialized_board, cnt = q.popleft()

        if serialized_board == answer:
            return cnt

        d_board = deserialize(serialized_board)

        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]

            if not bound_safe(ny, nx):
                continue

            d_board[ny][nx], d_board[y][x] = d_board[y][x], d_board[ny][nx]

            # 이미 해본거라면
            if serialize(d_board) in visit:
                d_board[ny][nx], d_board[y][x] = d_board[y][x], d_board[ny][nx]
                continue

            visit.add(serialize(d_board))
            q.append((ny, nx, serialize(d_board), cnt + 1))
            d_board[ny][nx], d_board[y][x] = d_board[y][x], d_board[ny][nx]

    return -1


print(sol())
