# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums)//2
        dummy = root = TreeNode(nums[len(nums)//2]) #0
        self.fill_Tree(0, mid-1, root, nums)
        self.fill_Tree(mid+1, len(nums)-1, root, nums)
        
        return dummy
        
    def fill_Tree(self, i, j, root, nums): 
        if i>j:
            return
        mid = i + (j-i)//2
        if nums[mid] <= root.val:
            root.left = TreeNode(nums[mid])
            root = root.left
        else:
            root.right = TreeNode(nums[mid])
            root = root.right
        self.fill_Tree(i, mid-1, root, nums)
        self.fill_Tree(mid+1, j, root, nums)
        
            