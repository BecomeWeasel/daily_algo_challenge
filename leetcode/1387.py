from collections import defaultdict


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        dp = defaultdict(lambda: -float("inf"))
        dp[1] = 0

        # 홀수같은 경우는 compute 함수를 통해서 직접 계산해줘야함
        # n//2 or n*3+1의 결과가 이미 계산되어있다면 바로 return 해버림
        def compute(n):
            nonlocal dp
            # recursive way
            if dp[n] >= 0:
                return dp[n]
            if n % 2:
                return compute(n * 3 + 1) + 1
            else:
                return compute(n // 2) + 1

            # iterative way
            """ 
            c = 0
            while n > 1:
                if n % 2 == 0:
                    n = n // 2
                    c += 1
                    # dp 범위내에서 계산되어 있다면
                    if 1 <= n <= 1000:
                        if dp[n] > 0:
                            return dp[n] + c
                else:
                    n = 3 * n + 1
                    c += 1
                    # dp 범위내에서 계산되어 있다면
                    if 1 <= n <= 1000:
                        if dp[n] > 0:
                            return dp[n] + c
            return c
            """

        for n in range(2, 1001):
            dp[n] = compute(n)
        return sorted(range(lo, hi + 1), key=lambda x: (dp[x], x))[k - 1]


Solution().getKth(12, 15, 2)
