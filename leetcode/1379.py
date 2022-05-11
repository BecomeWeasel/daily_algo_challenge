# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        def dfs(node,val):
            if not node:
                return None

            if node.val==val:
                return node

            else :
                for ret in dfs(node.left,target.val),dfs(node.right,target.val):
                    if ret:
                        return ret
        return dfs(cloned,target.val)

        """

        # if repeated values on the tree are allowed  -> 단순 node.val 비교로는 찾을수 없음
        # target까지의 방향을 기록해야함

        # target까지 가는 방향을 찾아줌
        def dfs(node, track):
            if not node:
                return None

            if node == target:
                return track

            else:
                l = dfs(node.left, track + ["L"])
                r = dfs(node.right, track + ["R"])

                return l if l else r

        def find(node, direct):
            # 원하는 노드에 도착
            if len(direct) == 0:
                return node
            #     다음 방향이 r이면 right subtree 검사,0번째 direct consume
            elif direct[0] == "R":
                return find(node.right, direct[1:])

            #   다음 방향이 l이면 left subtree 검사,0번째 direct consume
            else:
                return find(node.left, direct[1:])

        return find(cloned, dfs(original, []))
