# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #       no tree
        if not root:
            return 0

        # 만약 왼쪽 , 오른쪽 자식이 없으면
        # 1+0+0 (리프노드)
        # 한쪽만 없으면
        # 1+0+minDepth(root.right or left)
        if not root.left or not root.right:
            return 1 + self.minDepth(root.left) + self.minDepth(root.right)

        # 자식이 둘다 있다면 left subtree와 right subtree의 최솟값중 작은것을 출력
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
