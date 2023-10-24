# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        dummy = root
        
        def searchPosition(root, val):
            if not root:
                return
            
            if val < root.val:
                if root.left:
                    return searchPosition(root.left, val)
                else:
                    root.left = TreeNode(val)
                    return dummy
            else:
                if root.right:
                    return searchPosition(root.right, val)
                else:
                    root.right = TreeNode(val)
                    return dummy
            
            return root
        
        return searchPosition(root, val)