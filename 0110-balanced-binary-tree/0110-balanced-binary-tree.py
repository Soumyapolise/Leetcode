# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [root]
        
        def calc(root, level, res):
            if root is None:
                return 0
            
            if level > len(res):
                res.append("#")
            
            calc(root.left, level + 1, res)
            calc(root.right, level + 1, res)
            
            return len(res)
        
        while stack:
            node = stack.pop()
            res1, res2 = [], []
            l, r = 0, 0
            if node.left:
                l = calc(node.left, 1, res1)
                stack.append(node.left)
            
            if node.right:
                r = calc(node.right, 1, res2)
                stack.append(node.right)
            
            if abs(l-r) > 1:
                return False
            
            
            
        
        return True