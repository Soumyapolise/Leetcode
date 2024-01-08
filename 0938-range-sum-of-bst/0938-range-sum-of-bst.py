# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        
        self.dfs(root, low, high, res)
        
        return sum(res)
        
    def dfs(self, root, low, high, res):
        if root is None:
            return
        
        if root.val >= low and root.val <= high:
            res.append(root.val)
        
        self.dfs(root.left, low, high, res)
        self.dfs(root.right, low, high, res)