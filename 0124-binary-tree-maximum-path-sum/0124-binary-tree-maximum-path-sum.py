# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = float('-inf')
        
        def helper(root):
            nonlocal maxi
            
            if root is None:
                return 0
            
            l = max(helper(root.left), 0)
            r = max(helper(root.right), 0)
            
            maxi = max(maxi, l + r + root.val)
            
            return max(l + root.val, r + root.val)
        
        helper(root)
        return maxi
        
        
        