from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        R = len(board)
        C = len(board[0])

        visit = [[False for _ in range(C)] for _ in range(R)]

        def OOB(y, x):
            if not (0 <= y < R) or not (0 <= x < C):
                return True
            return False

        def bfs(q):
            nonlocal visit

            pieces = []

            min_y, min_x, max_x, max_y = float("inf"), float("inf"), -float("inf"), -float("inf")

            while q:
                y, x = q.popleft()
                pieces.append((y, x))

                min_y = min(min_y, y)
                min_x = min(min_x, x)

                max_y = max(max_y, y)
                max_x = max(max_x, x)

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]

                    if OOB(ny, nx):
                        continue

                    if not visit[ny][nx] and board[ny][nx] == "O":
                        visit[ny][nx] = True
                        q.append((ny, nx))
            if min_y == 0 or min_x == 0 or max_x == C - 1 or max_y == R - 1:
                return
            else:
                for pos_y, pos_x in pieces:
                    board[pos_y][pos_x] = "X"

        for i in range(R):
            for j in range(C):
                if board[i][j] == "O" and not visit[i][j]:
                    visit[i][j] = True
                    q = deque()
                    q.append((i, j))
                    bfs(q)
