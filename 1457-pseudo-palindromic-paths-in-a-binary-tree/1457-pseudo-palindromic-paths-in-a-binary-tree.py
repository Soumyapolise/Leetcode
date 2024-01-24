# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
#         res = []
        
#         self.dfs(root, res, [])
        
#         return len(res)
    
#     def dfs(self, root, res, curr):
#         if root is None:
#             return
        
#         # curr.append(root.val)
        
#         if root.left is None and root.right is None:
#             curr.append(root.val)
#             d = {}
#             for x in curr:
#                 if x not in d:
#                     d[x] = 0
#                 d[x] += 1
#             count = 0
            
#             for val in d.values():
#                 if val % 2 != 0:
#                     count += 1
#             # print(count, curr)
#             if count < 2:
#                 res.append("#")
            
#             return
        
#         self.dfs(root.left, res, curr + [root.val])
#         self.dfs(root.right, res, curr + [root.val])
#         if curr:
#             curr.pop()
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, bitmask):
        if root is None:
            return 0

        # Toggle the presence of the current value in the bitmask
        bitmask ^= 1 << root.val

        if root.left is None and root.right is None:
            # Check if the current path is pseudo-palindromic
            return 1 if bitmask == 0 or (bitmask & (bitmask - 1)) == 0 else 0

        left_paths = self.dfs(root.left, bitmask)
        right_paths = self.dfs(root.right, bitmask)

        return left_paths + right_paths
