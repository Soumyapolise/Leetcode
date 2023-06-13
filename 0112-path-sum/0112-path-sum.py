# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = []
        sums = 0
        def dfs(root, sums, res):
            if root is None:
                return
            sums += root.val
            if root.left is None and root.right is None and sums == targetSum:
                res.append(sums)
            
            dfs(root.left, sums, res)
            dfs(root.right, sums, res)
        
        
        dfs(root, sums, res)
        return len(res)>0
        
        