# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        q = deque()
        q.append([root, root.val, root.val])
        
        while q:
            curr, high, low = q.popleft()
            
            res = max(res, high - curr.val, curr.val - low)
            
            if curr.left:
                q.append([curr.left, max(high, curr.val), min(low, curr.val)])
            
            if curr.right:
                q.append([curr.right, max(high, curr.val), min(low, curr.val)])
        
        return res