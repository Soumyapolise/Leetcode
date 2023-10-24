# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        level = 1
        
        self.dfs(root, level, res)
        return res
    
    def dfs(self, root, level, res):
        if root is None:
            return
        
        if level > len(res):
            res.append(root.val)
        else:
            res[level-1] = max(res[level-1], root.val)
        
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)