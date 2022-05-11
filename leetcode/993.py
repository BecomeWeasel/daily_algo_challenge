# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:  # T:O(n) S:O(n)
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        # to maintain hashTable for storing both parent and height
        height = defaultdict(int)
        parent = defaultdict(int)

        """
        # O(n)
        def findParent(n,t)->TreeNode:
            if not n:
                return None
            else:
                if (n.left and n.left.val==t) or (n.right and n.right.val==t):
                    return n
                else:
                    return findParent(n.left,t) or findParent(n.right,t)
        """

        """ O(n)
        def getHeight(n,h,t)->int:
            if not n:
                return -1
            elif n.val==t:
                return h
            else:
                return max(getHeight(n.left,h+1,t),getHeight(n.right,h+1,t))
        """

        # O(1)
        def getHeight(t) -> int:
            return height[t]

        # O(1)
        def findParent(x) -> int:
            return parent[x]

        # O(n)
        def saveHeight(n, h):
            if not n:
                return
            else:
                height[n.val] = h
                saveHeight(n.left, h + 1)
                saveHeight(n.right, h + 1)

        # O(n)
        def saveParentValue(n):
            if not n:
                return
            else:
                if n.left:
                    parent[n.left.val] = n.val
                    saveParentValue(n.left)

                if n.right:
                    parent[n.right.val] = n.val
                    saveParentValue(n.right)

        saveHeight(root, 0)
        saveParentValue(root)

        if getHeight(x) == getHeight(y):
            return findParent(x) != findParent(y)
        else:
            return False
