# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def invert(root : TreeNode) -> TreeNode:
            if root:
                root.left,root.right=invert(root.right),invert(root.left)
                return root
            else:
                return None
            
        
        root=invert(root)
        
        return root