class Solution:
    def specialArray(self, nums: int) -> int:

        lo, hi = 0, len(nums) + 1
        ans = -1

        while lo < hi:
            count = 0

            mid = (lo + hi) // 2

            count += sum(1 for x in nums if x >= mid)

            if count == mid:
                ans = mid
                return ans
            elif count > mid:
                lo = mid + 1
            else:
                hi = mid

        return ans


print(Solution().specialArray([3, 6, 7, 7, 0]))
