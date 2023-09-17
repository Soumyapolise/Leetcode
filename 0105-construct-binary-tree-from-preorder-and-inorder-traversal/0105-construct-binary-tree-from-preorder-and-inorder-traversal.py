# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder == []:
            return None
        
        val = preorder.pop(0)
        root = TreeNode(val)
        
        idx = inorder.index(val)
        leftInorder = inorder[0:idx]
        rightInorder = inorder[idx+1:]
        
        root.left = self.buildTree(preorder, leftInorder)
        root.right = self.buildTree(preorder, rightInorder)
        
        return root
        
        