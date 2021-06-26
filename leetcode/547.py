from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        province, n = 0, len(isConnected)

        def dfs(city, visit):
            visit.add(city)

            for another, isConnect in enumerate(isConnected[city]):
                if another != city and isConnect == 1 and another not in visit:
                    dfs(another, visit)

        for city in range(n):
            if city not in visit:
                province += 1
                dfs(city, visit)

        return province