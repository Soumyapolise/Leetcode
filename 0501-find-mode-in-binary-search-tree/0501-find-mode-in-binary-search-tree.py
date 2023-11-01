# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        d = {}
        self.dfs(root, d)
        
        mode = max(d.values())
        res = []
        
        for k in d.keys():
            if d[k] == mode:
                res.append(k)
        
        return res
        
    def dfs(self, root, d):
        if not root:
            return
        
        if root.val in d:
            d[root.val] += 1
        else:
            d[root.val] = 1
        
        self.dfs(root.left, d)
        self.dfs(root.right, d)