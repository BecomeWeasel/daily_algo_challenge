class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0] * 38

        dp[1] = 1
        dp[2] = 1

        for k in range(3, n + 1):
            dp[k] = dp[k - 1] + dp[k - 2] + dp[k - 3]

        return dp[n]
