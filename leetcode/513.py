# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:  # T:O(n) S:O(h)
    def findBottomLeftValue(self, root: TreeNode) -> int:
        values = defaultdict(int)
        h = 0

        def reverse_inorder(root, h):
            if not root:
                return

            reverse_inorder(root.right, h + 1)
            values[h] = root.val
            reverse_inorder(root.left, h + 1)

        reverse_inorder(root, 0)

        # 가장 높이가 깊은 것중에서 가장 최근에 기록된것(가장 왼쪽에 기록된것)
        return values[max(values.keys())]