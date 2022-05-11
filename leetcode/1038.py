# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.values = []

        def dfs(node):
            if not node:
                return
            else:
                self.values.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        self.values.sort()

        #       현재 값보다 크거나 같은 값들의 합을 저장
        def add_dfs(node):
            if not node:
                return
            else:
                node.val = sum(self.values[self.values.index(node.val) :])
                add_dfs(node.left)
                add_dfs(node.right)

        add_dfs(root)

        return root
        """
        Reverse In-order traversal을 이용한 풀이
        self.total=0
        def dfs(node):
            if node:
                dfs(node.right)
                self.total+=node.val
                node.val=self.total
                dfs(node.left)
                
        dfs(root)
        
        return root
        """
