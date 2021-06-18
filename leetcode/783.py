# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def minDiffInBST(self, root: TreeNode) -> int:
    '''
    모든 node를 traverse한 다음 sort후 최소값 구하기 -> O(n)+O(nlogn)
    
    values = []

    def dfs(node):
      if not node.left and not node.right:
        values.append(node.val)
      else:

        if node.left:
          dfs(node.left)
        if node.right:
          dfs(node.right)

        values.append(node.val)

    min_diff = 987654321

    dfs(root)
    values.sort()
    idx = 0
    while idx < len(values) - 1:
      min_diff = min(min_diff, abs(values[idx] - values[idx + 1]))
      idx += 1
    return min_diff
    '''
    '''
        모든 node를 traverse 하는건 같지만,
        현재 node의 val와 left subtree의 rightmost (node.val보다 작은 값중에서 가장 큰 값)
        현재 node의 val와 right subtree의 leftmost (node.val보다 큰 값중에서 가장 작은 값)
        계속 비교 : O(n)*n time -> O(n^2)
    '''

    self.min_val = 100

    def rightmost(node):
      if node.right:
        return rightmost(node.right)
      else:
        return node.val

    def leftmost(node):
      if node.left:
        return leftmost(node.left)
      else:
        return node.val

    def dfs(node):
      if node.left:
        right_most = rightmost(node.left)
        print("node : " + str(node.val) + " rm: " + str(right_most))
        self.min_val = min(self.min_val, abs(right_most - node.val))
        dfs(node.left)
      if node.right:
        left_most = leftmost(node.right)
        print("node : " + str(node.val) + " lm: " + str(left_most))
        self.min_val = min(self.min_val, abs(left_most - node.val))
        dfs(node.right)

    dfs(root)

    return self.min_val