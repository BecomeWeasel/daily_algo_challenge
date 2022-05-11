# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        max_depth = -1

        depth_dict = defaultdict(list)

        def dfs(root, depth_dict):
            nonlocal max_depth
            if not root:
                return 0

            depth = max(dfs(root.right, depth_dict), dfs(root.left, depth_dict)) + 1

            max_depth = max(depth, max_depth)

            depth_dict[depth].append(root.val)

            return depth

        dfs(root, depth_dict)
        answer = []

        for i in range(1, max_depth + 1):
            answer.append(depth_dict[i])

        return answer
