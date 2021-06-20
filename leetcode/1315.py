# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, grandparent: TreeNode, parent: TreeNode):
            if not node:
                return 0

            ret = 0

            if grandparent and grandparent.val % 2 == 0:
                ret += node.val

            return ret + dfs(node.left, parent, node) + dfs(
                node.right, parent, node)

        return dfs(root, None, None)
