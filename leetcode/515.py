# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:  # T:O(n) S:O(h)
    def largestValues(self, root: TreeNode) -> List[int]:
        # int로 두면 0이 기본값으로 들어가는데
        # node들의 값이 0보다 작을 수 있음
        values = defaultdict(lambda: -float("inf"))
        h = 0

        def preorder(root, h):
            if not root:
                return

            values[h] = max(values[h], root.val)
            preorder(root.left, h + 1)
            preorder(root.right, h + 1)

        # dict에 key의 순서를 보장하기 위해서 preorder
        preorder(root, 0)

        return values.values()
