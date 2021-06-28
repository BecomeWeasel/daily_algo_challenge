class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        ans = -1
        while lo <= hi:

            mid = (lo + hi) // 2

            if (mid * (mid + 1)) / 2 <= n:
                lo = mid + 1
                ans = max(ans, mid)
            else:
                hi = mid - 1

        return ans
