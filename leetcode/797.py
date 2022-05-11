class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1

        result = []

        def dfs(node, path):
            if node == target:
                result.append(path)
            else:
                for another_node in graph[node]:
                    dfs(another_node, path + [another_node])

        for adjacent_node in graph[0]:
            dfs(adjacent_node, [0, adjacent_node])

        return result
