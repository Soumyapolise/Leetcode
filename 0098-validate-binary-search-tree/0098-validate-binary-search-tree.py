# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.dfs(root, res)
        
        num = res[0]
        
        for n in res[1:]:
            if n <= num:
                return False
            num = n
        
        return True
        
    def dfs(self, root, res):
        if not root:
            return
        
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
        
#         def calc(ref, root, left, right):
#             if root is None:
#                 return True
            
#             if left:
#                 if root.val >= ref:
#                     return False
            
#             if right:
#                 if root.val <= ref:
#                     return False
            
#             return calc(root.val, root.left, True, False) and calc(root.val, root.right, False, True)
        
#         return calc(root.val, root.left, True, False) and calc(root.val, root.right, False, True)

    
    
        