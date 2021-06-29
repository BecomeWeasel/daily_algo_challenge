class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0, 0, 0, 0, 0, 0] for _ in range(51)]

        dp[1] = [0, 1, 1, 1, 1, 1]

        for k in range(2, n + 1):
            for j in range(1, 5 + 1):
                dp[k][j] = sum(dp[k - 1][x] for x in range(j, 5 + 1))
        return sum(dp[n])
