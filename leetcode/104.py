# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        else:
            if not root.left and not root.right:
                return 1
            else:
                left_high = 0 if not root.left else self.maxDepth(root.left)
                right_high = 0 if not root.right else self.maxDepth(root.right)

                return max(left_high, right_high) + 1
