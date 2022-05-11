class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(45 + 1)]

        dp[1] = 1
        dp[2] = 2

        """
        # top down
        def getDp(k):
            # 미리 계산되었다면
            if dp[k]>0 or (k==0)  :
                return dp[k]
            
            dp[k]=getDp(k-1)+getDp(k-2)
            
            return dp[k]
            
            
        return getDp(n)
        """

        # bottom up
        for k in range(3, n + 1):
            dp[k] = dp[k - 1] + dp[k - 2]
        return dp[n]
