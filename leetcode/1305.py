# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:  # O(n+m)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        values1, values2 = [], []

        def traversal(root, values):  # O(n)
            if not root:
                return
            else:
                traversal(root.left, values)
                values.append(root.val)
                traversal(root.right, values)

        traversal(root1, values1)  # n nodes
        traversal(root2, values2)  # m nodes

        def merge(arr1, arr2):  # O(n+m)

            len1 = len(arr1)
            len2 = len(arr2)
            merged_list = [None for _ in range(len1 + len2)]

            i, j, k = 0, 0, 0

            while i < len1 and j < len2:
                if arr1[i] <= arr2[j]:
                    merged_list[k] = arr1[i]
                    k += 1
                    i += 1
                else:
                    merged_list[k] = arr2[j]
                    k += 1
                    j += 1

            while i < len1:
                merged_list[k] = arr1[i]
                k += 1
                i += 1

            while j < len2:
                merged_list[k] = arr2[j]
                k += 1
                j += 1

            return merged_list

        return merge(values1, values2)
