# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def traverse(root):
            nonlocal res
            
            if not root:
                return 0, 0
            
            left_sum, left_count = traverse(root.left)
            right_sum, right_count = traverse(root.right)
            
            s = root.val + left_sum + right_sum
            c = 1 + left_count + right_count
            
            if s // c == root.val:
                res += 1
            
            return s, c
        
        traverse(root)
        
        return res