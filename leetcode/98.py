# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def isValidBST(self, root):

        elements = []

        def inorder(root):
            nonlocal elements

            if not root:
                return

            inorder(root.left)
            elements.append(root.val)
            inorder(root.right)

        inorder(root)

        if len(elements) <= 1:
            return True
        else:
            prev = elements[0]

            for e in elements[1:]:
                if not e > prev:
                    return False
                prev = e
            return True
