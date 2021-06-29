class Solution:
    def maxSubArray(self, nums: int) -> int:


        ans,sumValue=nums[0],nums[0]

        for i in range(1,len(nums)):
            if sumValue<0:
                sumValue=nums[i]
            else:
                sumValue+=nums[i]
            ans=max(ans,sumValue)
        return ans
