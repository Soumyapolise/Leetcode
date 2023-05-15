# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 1
        self.dfs(root, res, level)
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
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