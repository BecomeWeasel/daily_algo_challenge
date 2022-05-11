# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from bisect import bisect_left


class FindElements:  # O(n)
    def __init__(self, root: TreeNode):
        # root 노드를 find 함수에 사용될 클래스 멤버로 저장,
        self.node = root
        # lookup을 빠르게 하기 위해서 set 사용
        self.values = {0}

        root.val = 0

        q = deque()
        q.append(root)

        while q:
            front_node = q.popleft()

            if front_node.left:
                front_node.left.val = front_node.val * 2 + 1
                self.values.add(front_node.val * 2 + 1)
                q.append(front_node.left)
            if front_node.right:
                front_node.right.val = front_node.val * 2 + 2
                self.values.add(front_node.val * 2 + 2)
                q.append(front_node.right)

    def find(self, target: int) -> bool:
        """
        # TLE
        만약 트리에 절대 없는 값(음수)를 찾을때는 O(1)이지만 나머지는 O(n)

        if target<0:
            return False

        def recursive_find(t:int,node:TreeNode)->bool:
            if not node:
                return False

            # 찾으면
            elif node.val==t:
                return True
            # left subtree와 right subtree에 대해서 recursive한 find
            else:
                return recursive_find(target,node.left) or recursive_find(target,node.right)


        return recursive_find(target,self.node)
        """
        # O(1)
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
