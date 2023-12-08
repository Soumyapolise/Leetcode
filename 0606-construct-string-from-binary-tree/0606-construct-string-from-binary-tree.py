# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        ch = ""
        self.dfs(root, res)
        
        res = "".join(res)
        
        return res
    def dfs(self, root, res):
        if root:
            if root.left or root.right:
                res += [str(root.val) + "("]
                self.dfs(root.left, res)
                res += [")"]
                if root.right:
                    res += ["("]
                    self.dfs(root.right, res)
                    res += [")"]
            else:
                res += [str(root.val)]
        
            
            
        
        
            
            
            