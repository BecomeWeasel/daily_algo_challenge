class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        start_color = image[sr][sc]

        R, C = len(image), len(image[0])

        def dfs(y, x):
            image[y][x] = newColor

            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]

                if 0 <= ny < R and 0 <= nx < C:
                    if image[ny][nx] == start_color:
                        dfs(ny, nx)

        # we don't have visited matrix so
        # without this statement,
        # fallen into infinited loop
        if start_color != newColor:
            dfs(sr, sc)

        return image
