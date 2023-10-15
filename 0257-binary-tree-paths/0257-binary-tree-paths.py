# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.dfs(root, res, "")
        return res
    
    def dfs(self, root, res, seq):
        if root is None:
            return
        
        seq += str(root.val) + "->"
        
        if root.left is None and root.right is None:
            seq = seq[0:-2]
            res.append(seq)
            return
        
        self.dfs(root.left, res, seq)
        self.dfs(root.right, res, seq)