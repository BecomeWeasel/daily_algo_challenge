class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        r, c = len(grid), len(grid[0])

        def getPerimeter(y, x):
            nonlocal grid, r, c
            count = 0

            if y == 0:
                count += 1
            if y == r - 1:
                count += 1
            if x == 0:
                count += 1
            if x == c - 1:
                count += 1

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]

                if 0 <= ny < r and 0 <= nx < c:
                    if grid[ny][nx] == 0:
                        count += 1
            return count

        visit = set()
        ans = 0

        def dfs(y, x):
            nonlocal visit, grid, ans

            ans += getPerimeter(y, x)

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]

                if not (0 <= ny < r and 0 <= nx < c):
                    continue

                if grid[ny][nx] == 1 and (ny, nx) not in visit:
                    visit.add((ny, nx))
                    dfs(ny, nx)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 and (i, j) not in visit:
                    visit.add((i, j))
                    dfs(i, j)
        return ans
