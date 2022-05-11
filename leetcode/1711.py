from math import log2, ceil, pow, comb
from collections import defaultdict


class Solution:  # T:O(nlogn) S:O(n)
    def countPairs(self, deliciousness: int) -> int:
        answer = 0
        len_deliciousness = len(deliciousness)

        freq = defaultdict(int)

        for num in deliciousness:
            freq[num] += 1

        if len_deliciousness == 1:
            return 0

        deliciousness.sort()
        # 리스트 안의 가장 큰 두 값보다 작거나 같은 2의 제곱수까지만 검사하면 됨
        bound = pow(2, ceil(log2(deliciousness[-1] + deliciousness[-2])))

        power_of_2s = 1

        # 중복 제거
        deliciousness = list(set(deliciousness))
        deliciousness.sort()
        len_deliciousness = len(deliciousness)

        # 투포인터 활용
        while power_of_2s <= bound:

            s, e = 0, len_deliciousness - 1
            while s <= e:
                # 두 포인터가 가리키고 있는 값이 더해서 2의 제곱수라면
                if deliciousness[s] + deliciousness[e] == power_of_2s:
                    # s==e가 같을때도 element들이 unique하지 않기때문에
                    # (1,1)같은 경우도 고려해줘야함
                    # 이때는 nC2만큼의 경우의 수가 있음 ( n : 등장빈도)
                    if s == e:
                        if freq[deliciousness[s]] >= 2:
                            answer += comb(freq[deliciousness[s]], 2)
                        break
                    answer += freq[deliciousness[s]] * freq[deliciousness[e]]
                    s += 1
                # 더한 값이 작으면 왼쪽으로 커서 옮기고
                elif deliciousness[s] + deliciousness[e] < power_of_2s:
                    s += 1
                # 더한 값이 크면 오른쪽으로 커서 옮김
                else:
                    e -= 1
            # 다음 제곱수 계산
            power_of_2s *= 2
        return answer % (1000000000 + 7)
