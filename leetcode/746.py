class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        num_stairs = len(cost)
        cost.append(0)
        dp = [0 for _ in range(num_stairs + 1)]

        dp[0] = cost[0]
        dp[1] = cost[1]

        # bottom up

        for n in range(2, num_stairs + 1):
            dp[n] = min(dp[n - 2], dp[n - 1]) + cost[n]
        return dp[num_stairs]

        """
        # top down
        def getDp(n):
            nonlocal dp,cost

            if dp[n]>0  or (n==0 or n==1):
                return dp[n]

            dp[n]=min(getDp(n-2),getDp(n-1))+cost[n]
            
            return dp[n]
        
        return getDp(num_stairs)
        """
