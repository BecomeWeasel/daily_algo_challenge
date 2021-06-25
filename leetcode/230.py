# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: # T:O(n) (inorder) , O(n^2) (check num of nodes in left subtree)
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        ''' 서브트리마다 왼쪽에 있는 노드 개수를 확인
        # O(n^2)
        def getNumOfTree(n):
                if not n:
                    return 0
                else:
                    return 1+getNumOfTree(n.left)+getNumOfTree(n.right)
                        
        def helper(n:TreeNode,k:int)->int:
            if not n:
                return 1
            
            
            lt=getNumOfTree(n.left)
                        
            # 나보다 작은 값들이 k-1개면 내가 k번째
            if lt+1==k:
                return n.val
            # 나보다 작은 값들이 k개보다 많으면, 왼쪽에서 찾아야함, k는 그대로
            elif lt+1>k:
                return helper(n.left,k)
            # 나보다 작은 값들이 k개보다 적으면, 나보다 큰쪽에서 찾아야함. k는 k-lt-1
            else:
                return helper(n.right,k-(lt+1))
            
        return helper(root,k)
        '''
        self.count=0
        self.ret=-1
        
        # O(n) 
        def inorder(root,k):
            if not root:
                return
            inorder(root.left,k)
            
            self.count+=1
            
            if self.count==k:
                self.ret=root.val
            
            inorder(root.right,k)
    
        inorder(root,k)
        
        return self.ret
            
        
        
            
        