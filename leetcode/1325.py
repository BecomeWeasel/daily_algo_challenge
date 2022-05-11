# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  # T:O(N)
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root:
            return None

        # 자식이 없어져서 내가 리프가 될수 있음
        # 자식을 먼저 체크하고 나 자신을 체크해야하니 postorder
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # 자식도 없고(윗 단계에서 사라졌을수가 있음) 내가 target이라면
        # 나 자신을 삭제
        if root.val == target and not root.left and not root.right:
            return None
        return root
