"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:  # O(n)
    def levelOrder(self, root: "Node") -> List[List[int]]:
        result = []

        if not root:
            return result

        q = deque()
        q.append([root, 0])

        while q:
            node, h = q.popleft()

            if len(result) <= h:
                result.append(list())
            result[h].append(node.val)

            for child in node.children:
                q.append([child, h + 1])

        return result
