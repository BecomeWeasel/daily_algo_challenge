class Solution:
    """# T:O(n^2)
    def countNegatives(self, grid) -> int:
        return sum(list(map(lambda x: sum(1 if x[j] < 0 else 0 for j in range(len(grid[0]))), grid)))
    """

    # T:O(n+m)
    def countNegatives(self, grid):
        i = len(grid) - 1
        j = 0
        answer = 0
        while i >= 0 and j < len(grid[0]):

            # 가로,세로 모두 non-increasing이기때문에
            # i는 맨 아래서부터 시작
            if grid[i][j] < 0:
                answer += len(grid[0]) - j
                i -= 1
            else:
                j += 1
        return answer
