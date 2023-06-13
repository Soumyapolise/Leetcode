# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sums = 0
        def dfs(root, sums):
            if root is None:
                return
            sums += root.val
            if root.left is None and root.right is None:
                return sums == targetSum
            
            return dfs(root.left, sums) or dfs(root.right, sums)
        
        
        return dfs(root, sums)
        
        
        