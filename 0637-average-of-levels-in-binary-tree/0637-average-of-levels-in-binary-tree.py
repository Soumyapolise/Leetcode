# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        level = 1
        
        self.dfs(root, res, level)
        for i in range(len(res)):
            res[i] = sum(res[i])/len(res[i])
        
        return res
        
    def dfs(self, root, res, level):
        if root is None:
            return
        
        if level>len(res):
            res.append([root.val])
        else:
            res[level-1] += [root.val]
        
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)