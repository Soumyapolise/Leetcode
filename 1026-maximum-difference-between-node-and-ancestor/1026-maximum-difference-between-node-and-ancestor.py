# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque()
        queue.append([root, root.val, root.val])
        
        while queue:
            curr, high, low = queue.popleft()
            
            diff1 = high - curr.val
            diff2 = curr.val - low
            
            res = max(res, diff1, diff2)
            
            if curr.left:
                queue.append([curr.left, max(curr.val, high), min(curr.val, low)])
            
            if curr.right:
                queue.append([curr.right, max(curr.val, high), min(curr.val, low)])
        
        return res