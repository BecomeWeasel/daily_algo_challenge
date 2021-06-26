class Solution: # T:O(w*h) S:O(1)
    def countBattleships(self, board: List[List[str]]) -> int:
        num_ships = 0

        w, h = len(board[0]), len(board)

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        def dfs(y, x):
            nonlocal board

            board[y][x] = '.'

            for k in range(4):

                ny, nx = y + dy[k], x + dx[k]

                if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == 'X':
                    dfs(ny, nx)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'X':
                    num_ships += 1
                    dfs(i, j)

        return num_ships