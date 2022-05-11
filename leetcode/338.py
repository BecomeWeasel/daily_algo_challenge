import math


class Solution:
    # 우선 i를 이진수로 표현했을때 자릿수에 기반해서 구간이 나뉘어지고
    # 구간의 길이를 k라 할때 0~2/k까지는 직전 구간과 동일하고
    # 2/k+1~k까지는 직전구간에 + 1
    def countBits(self, n: int) -> List[int]:
        ans = [0, 1]

        if n > 0:
            closest = int(math.pow(2, math.ceil(math.log2(n))))
            while len(ans) <= closest:
                ans = ans + list(map(lambda x: x + 1, ans))
            return ans[: n + 1]
        else:
            return [0]
