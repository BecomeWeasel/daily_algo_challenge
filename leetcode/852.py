class Solution: # T:O(log n)
    def peakIndexInMountainArray(self, arr) -> int:
        ''' T:O(n)
        for idx in range(len(arr)-1):
            if arr[idx]>arr[idx+1]:
                return idx
        '''
        lo,hi=0,len(arr)-1
        
        while lo<hi:
            
            mid=(lo+hi)//2
            
            # mid에서도 여전히 증가한다면
            # mid보다 오른쪽에 peak이 있음
            if arr[mid]<arr[mid+1]:
                lo=mid+1
            # 감소가 시작되었다면
            # mid보다 왼쪽에 peak이 있음
            else:
                hi=mid
        return lo
                
                
            
Solution().peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19])