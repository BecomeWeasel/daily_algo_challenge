# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        #  먼저 트리의 detph를 구해야함
        def getDepth(root):
            if not root:
                return 0
            else:
                return 1 + max(getDepth(root.left), getDepth(root.right))

        tree_depth = getDepth(root)

        def dfs(node, depth, tree_depth):
            #  없는 노드에 대한 호출
            if not node:
                return 0
            #
            if not node.right and not node.left:
                #  리프인데 depth가 가장 깊다면
                if depth == tree_depth:
                    return node.val
                #       리프지만 depth가 가장 깊지 않다면
                else:
                    return 0
            else:
                return dfs(node.left, depth + 1, tree_depth) + dfs(
                    node.right, depth + 1, tree_depth
                )

        return dfs(root, 1, tree_depth)


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

# 최대 높이를 구하지 않고 defaultdict 이용해서
# depth에 해당하는 리프노드의 값들을 더해줌
# time : O(n)
# space : O(h)
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.dic=defaultdict(int)
        
        def dfs(node,depth):
            if not node:
                return 0
            
            if not node.left and not node.right:
                self.dic[depth]+=node.val
            
            else:
                dfs(node.right,depth+1)
                dfs(node.left,depth+1)
        dfs(root,1)
                
        return self.dic[max(self.dic)]

"""
