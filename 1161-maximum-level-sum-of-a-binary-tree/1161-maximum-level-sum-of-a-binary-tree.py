# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []
        level = 1
        self.dfs(root, res, level)
        
        value = max(res)
        for i in range(len(res)):
            if res[i] == value:
                return i+1
        
        
        
        
    def dfs(self, root, res, level):
        if root is None:
            return 
        
        if level>len(res):
            res.append(root.val)
        else:
            res[level-1] += root.val
        
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)