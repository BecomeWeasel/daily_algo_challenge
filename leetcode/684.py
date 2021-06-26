class Solution:  # T:O(V*E) S:O(V)
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i + 1: i + 1 for i in range(n)}

        def find(x):
            nonlocal parent
            if parent[x] != x:
                return find(parent[x])
            else:
                return x

        def union(x, y):
            nonlocal parent
            x = find(x)
            y = find(y)

            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        result = []

        for src, dest in edges:
            # 다른 부모를 가진다는 것은 합쳐야함
            if find(src) != find(dest):
                union(src, dest)
            # 이미 부모가 같다면 (같은 set) redundant edge
            else:
                # 왜 다른 edge는 안봐도 되냐면, 트리는 최대 정확히 n-1개의 edge를 가지고
                # edge 개수는 n개이니 redundant edge는 오직 1개
                return [src, dest]
