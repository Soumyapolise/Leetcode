# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.dfs(root, res, 1)
        print(res)
        for i in range(len(res)):
            if len(res[i]) != len(set(res[i])):
                return False
            if i%2 == 0:
                for x in res[i]:
                    if x % 2 == 0:
                        return False
                if res[i] != sorted(res[i]):
                    return False
            else:
                for x in res[i]:
                    if x % 2 != 0:
                        return False
                if res[i] != sorted(res[i])[::-1]:
                    return False
            
        return True
        
    def dfs(self, root, res, level):
        if root is None:
            return 
        
        if level > len(res):
            res.append([root.val])
        else:
            res[level-1] += [root.val]
        
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)
        