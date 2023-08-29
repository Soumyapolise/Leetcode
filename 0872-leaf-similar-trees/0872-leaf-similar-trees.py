# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1, res2 = [], []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        
        return res1 == res2
        
    def dfs(self, root, res):
        if root is None:
            return
        
        if root.left is None and root.right is None:
            res.append(root.val)
        
        self.dfs(root.left, res)
        self.dfs(root.right, res)