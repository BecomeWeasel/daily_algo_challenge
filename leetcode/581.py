class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        og=sorted([x for x in nums])
        start=0
        end=len(nums)-1
        for i,n in enumerate(og):
            if nums[i]==n:
                start+=1
                continue
            else:
                break
        
        for i in range(len(nums)-1,-1,-1):
            if og[i]==nums[i]:
                end-=1
                continue
            else:
                break
        
        if end<=start:
            return 0
        
        return end-start+1