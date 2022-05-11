from collections import deque


class Solution:  # T:O(number of island)
    def closedIsland(self, grid: int) -> int:

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        r, c = len(grid), len(grid[0])

        visit = set()

        def turnIslandToWater(y, x):
            nonlocal visit, grid, r, c
            visit.add((y, x))
            grid[y][x] = 1
            q = deque()
            q.append((y, x))

            while q:
                y, x = q.popleft()

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]

                    if not (0 <= ny < r and 0 <= nx < c):
                        continue

                    # 옆에 붙어있는 땅(0)도 물(1)로 바꿔줌
                    if grid[ny][nx] == 0 and (ny, nx) not in visit:
                        visit.add((ny, nx))
                        grid[ny][nx] = 1
                        q.append((ny, nx))

        # 가장자리 섬들을 조사
        for y in range(r):
            if y == 0 or y == r - 1:
                for x in range(c):
                    if grid[y][x] == 0 and (y, x) not in visit:
                        turnIslandToWater(y, x)
            else:
                for x in [0, c - 1]:
                    if grid[y][x] == 0 and (y, x) not in visit:
                        turnIslandToWater(y, x)

        def bfs(y, x):
            nonlocal visit, grid, r, c
            visit.add((y, x))
            q = deque()
            q.append((y, x))

            while q:
                y, x = q.popleft()

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]

                    if not (0 <= ny < r and 0 <= nx < c):
                        continue

                    # 옆에 붙어있는 땅(0) 방문
                    if grid[ny][nx] == 0 and (ny, nx) not in visit:
                        visit.add((ny, nx))
                        grid[ny][nx] = 1
                        q.append((ny, nx))

        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0 and (i, j) not in visit:
                    bfs(i, j)
                    ans += 1
        return ans
