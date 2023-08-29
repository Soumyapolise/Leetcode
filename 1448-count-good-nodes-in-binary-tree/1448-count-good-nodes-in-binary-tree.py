# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxi = root.val
        res = []
        self.dfs(root, res, maxi)
        return len(res)
    
    def dfs(self, root, res, maxi):
        if not root:
            return
        
        if root.val >= maxi:
            res.append(root.val)
            maxi = root.val
        
        self.dfs(root.left, res, maxi)
        self.dfs(root.right, res, maxi)
        