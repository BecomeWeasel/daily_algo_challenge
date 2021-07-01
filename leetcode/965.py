# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # T:O(n)
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        
        def traversal(root,t):
            if not root:
                return True
            
            
            if root.val==t:
                return traversal(root.left,t) and traversal(root.right,t)
            else:
                return False
            
        
        return traversal(root,root.val)