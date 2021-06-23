# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import defaultdict


class Solution:  # O(V*E)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        new_nodes = {node.val}
        # edge_set contains all the edges (actually duplicated ones)
        edge_set = []

        def dfs(node, visited):
            for adjacent_node in node.neighbors:
                edge_set.append([node.val, adjacent_node.val])

                if adjacent_node.val not in new_nodes:
                    new_nodes.add(adjacent_node.val)

                if not visited[adjacent_node.val]:
                    visited[adjacent_node.val] = True
                    dfs(adjacent_node, visited)

        for vertex in node.neighbors:
            visited = defaultdict(bool)
            visited[vertex.val] = True
            dfs(vertex, visited)

        adjacency_list = [[] for i in range(len(new_nodes))]

        for edges in edge_set:
            src, dest = edges

            if dest not in adjacency_list[src - 1]:
                adjacency_list[src - 1].append(dest)

        # nodes 만들기
        copied_nodes = {x: Node(x) for x in range(1, len(new_nodes) + 1)}

        for val in copied_nodes:
            for node_num in adjacency_list[val - 1]:
                copied_nodes[val].neighbors.append(copied_nodes[node_num])

        return copied_nodes[node.val]


'''
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import defaultdict

class Solution: # O(V+E)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        # new_nodes가 일종의 visit 역할을 수행
        # new_nodes안에 node가 잇다면 dfs(node)가 이미 수행된것
        new_nodes={node.val:Node(node.val)}
        
        def dfs(node,new_nodes): # O(V+E)
            for neighbor in node.neighbors:
                if neighbor.val not in new_nodes:
                    new_nodes[neighbor.val]=Node(neighbor.val)
                    # dfs 함수를 호출할때 인자는
                    # 새로 만들어진 neighbor가 아닌 원래 있던 neighbor
                    dfs(neighbor,new_nodes)
                new_nodes[node.val].neighbors.append(new_nodes[neighbor.val])
                
            
        dfs(node,new_nodes)
            
            
        
        return new_nodes[node.val]
'''
