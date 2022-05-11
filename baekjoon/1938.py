from sys import stdin
from collections import deque

N = int(stdin.readline())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


class log:
    def __init__(self, is_vertical, center=None) -> None:
        self.center = center
        self.is_vertical = is_vertical

    def __str__(self) -> str:
        return str(self.center) + " is vertical " + str(self.is_vertical)


def sol():
    global N, log
    board = []

    for _ in range(N):
        board.append(list(stdin.readline().rstrip()))
    tree = None
    endpoint = None

    def getTree(N, board):
        for i in range(N):
            for j in range(N):
                # 나무가 초기상태에서 세로로 있을때
                if board[i][j] == "B" and i + 1 < N and board[i + 1][j] == "B":
                    tree = log(True, (i + 1, j))
                    return tree
                elif board[i][j] == "B" and j + 1 < N and board[i][j + 1] == "B":
                    tree = log(False, (i, j + 1))
                    return tree

    def getEndPoint(N, board):
        for i in range(N):
            for j in range(N):
                # 끝나는점이 초기상태에서 세로로 있을때
                if board[i][j] == "E" and i + 1 < N and board[i + 1][j] == "E":
                    endpoint = log(True, (i + 1, j))
                    return endpoint
                elif board[i][j] == "E" and j + 1 < N and board[i][j + 1] == "E":
                    endpoint = log(False, (i, j + 1))
                    return endpoint

    tree = getTree(N, board)
    endpoint = getEndPoint(N, board)

    visit = [[[False for _ in range(N)] for _ in range(N)] for _ in range(2)]

    visit[tree.is_vertical][tree.center[0]][tree.center[1]]

    def is_rotate_safe(is_vertical, y, x, board):
        if is_vertical:
            if (not (0 <= x - 1 < N)) or (not (0 <= x + 1 < N)):
                return False
            for i in range(y - 1, y + 1 + 1, 1):
                if board[i][x - 1] == "1":
                    return False
            for i in range(y - 1, y + 1 + 1, 1):
                if board[i][x + 1] == "1":
                    return False
            return True
        else:
            if (not (0 <= y - 1 < N)) or (not (0 <= y + 1 < N)):
                return False
            for j in range(x - 1, x + 1 + 1, 1):
                if board[y - 1][j] == "1":
                    return False
            for j in range(x - 1, x + 1 + 1, 1):
                if board[y + 1][j] == "1":
                    return False
            return True

    q = deque()
    q.append((tree, 0))
    while q:
        head, count = q.popleft()
        if head.center == endpoint.center and head.is_vertical == endpoint.is_vertical:
            return count

        c_y, c_x = head.center

        if head.is_vertical:
            # 위로 갈때
            if (
                (0 <= c_y - 1 - 1 < N)
                and not visit[True][c_y - 1][c_x]
                and board[c_y - 1 - 1][c_x] != "1"
            ):
                visit[True][c_y - 1][c_x] = True
                q.append((log(True, (c_y - 1, c_x)), count + 1))
            # 아래로 갈때
            if (
                (0 <= c_y + 1 + 1 < N)
                and not visit[True][c_y + 1][c_x]
                and board[c_y + 1 + 1][c_x] != "1"
            ):
                visit[True][c_y + 1][c_x] = True
                q.append((log(True, (c_y + 1, c_x)), count + 1))

            # 우로 갈때

            if (
                (0 <= c_x + 1 < N)
                and not visit[True][c_y][c_x + 1]
                and board[c_y - 1][c_x + 1] != "1"
                and board[c_y][c_x + 1] != "1"
                and board[c_y + 1][c_x + 1] != "1"
            ):
                visit[True][c_y][c_x + 1] = True
                q.append((log(True, (c_y, c_x + 1)), count + 1))

            # 좌로 갈때
            if (
                (0 <= c_x - 1 < N)
                and not visit[True][c_y][c_x - 1]
                and board[c_y - 1][c_x - 1] != "1"
                and board[c_y][c_x - 1] != "1"
                and board[c_y + 1][c_x - 1] != "1"
            ):
                visit[True][c_y][c_x - 1] = True
                q.append((log(True, (c_y, c_x - 1)), count + 1))

            # 회전할때

            if not visit[False][c_y][c_x] and is_rotate_safe(True, c_y, c_x, board):
                visit[False][c_y][c_x] = True
                q.append((log(False, (c_y, c_x)), count + 1))

        else:
            # 위로 갈때
            if (
                (0 <= c_y - 1 < N)
                and not visit[False][c_y - 1][c_x]
                and board[c_y - 1][c_x - 1] != "1"
                and board[c_y - 1][c_x] != "1"
                and board[c_y - 1][c_x + 1] != "1"
            ):
                visit[False][c_y - 1][c_x] = True
                q.append((log(False, (c_y - 1, c_x)), count + 1))
            # 아래로 갈때
            if (
                (0 <= c_y + 1 < N)
                and not visit[False][c_y + 1][c_x]
                and board[c_y + 1][c_x - 1] != "1"
                and board[c_y + 1][c_x] != "1"
                and board[c_y + 1][c_x + 1] != "1"
            ):
                visit[False][c_y + 1][c_x] = True
                q.append((log(False, (c_y + 1, c_x)), count + 1))
            # 우로 갈때
            if (
                (0 <= c_x + 1 + 1 < N)
                and not visit[False][c_y][c_x + 1]
                and board[c_y][c_x + 1 + 1] != "1"
            ):
                visit[False][c_y][c_x + 1] = tree
                q.append((log(False, (c_y, c_x + 1)), count + 1))
            # 좌로 갈때
            if (
                (0 <= c_x - 1 - 1 < N)
                and not visit[False][c_y][c_x - 1]
                and board[c_y][c_x - 1 - 1] != "1"
            ):
                visit[False][c_y][c_x - 1] = tree
                q.append((log(False, (c_y, c_x - 1)), count + 1))

            # 회전할때
            if not visit[True][c_y][c_x] and is_rotate_safe(False, c_y, c_x, board):
                visit[True][c_y][c_x] = True
                q.append((log(True, (c_y, c_x)), count + 1))

    return 0


print(sol())
