# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        mini = 10**5
        self.dfs(root, res)
        res = sorted(res)
        for i in range(1, len(res)):
             mini = min(mini, res[i]-res[i-1])
        
        return mini
    
    def dfs(self, root, res):
        if root is None:
            return
        
        res.append(root.val)
        
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        
            