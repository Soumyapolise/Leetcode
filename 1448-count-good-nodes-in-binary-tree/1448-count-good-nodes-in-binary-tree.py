# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        maxi = root.val
        
        self.dfs(root, res, maxi)
        # print(res)
        return len(res)
        
    def dfs(self, root, res, maxi):
        if root is None:
            return
        maxi = max(maxi, root.val)
        if root.val >= maxi:
            res.append([root.val, maxi])
        
        self.dfs(root.left, res, maxi)
        self.dfs(root.right, res, maxi)
        
        