# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 1
        res = 0

        def dfs(root, level):
            nonlocal res
            
            if root is None:
                return 

            res = max(res, level)

            dfs(root.left, level+1)
            dfs(root.right, level+1)
            
        dfs(root, level)
        return res