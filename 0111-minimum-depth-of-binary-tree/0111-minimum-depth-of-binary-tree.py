# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        level = 1
        depths = []
        if root is None:
            return 0
        self.dfs(root, depths, level)
        
        return min(depths)
        
    def dfs(self, root, depths, level):
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            depths.append(level)
        
        self.dfs(root.left, depths, level+1)
        self.dfs(root.right, depths, level+1)