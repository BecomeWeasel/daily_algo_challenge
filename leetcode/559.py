"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        if root.children:
            return max(self.maxDepth(child) for child in root.children) + 1

        else:
            return 1
