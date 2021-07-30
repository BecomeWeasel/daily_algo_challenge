class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        sigma=sum(nums)
        
        N=len(nums)
        dp=[0 for _ in range(N)]
        
        for i in range(N):
            dp[0]+=i*nums[i]
        
        
        for n in range(1,N):
            dp[n]=dp[n-1]+sigma-N*nums[N-n]
        
        return max(dp)
        