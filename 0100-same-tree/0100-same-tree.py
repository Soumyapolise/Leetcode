# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#         res1, res2 = [], []
#         self.dfs(p, res1)
#         self.dfs(q, res2)
        
#         return res1==res2
        
#     def dfs(self, root, res):
#         if not root:
#             res.append("null")
#             return
        
#         res.append(root.val)
        
#         self.dfs(root.left, res)
#         self.dfs(root.right, res)
        
            
        
        
        