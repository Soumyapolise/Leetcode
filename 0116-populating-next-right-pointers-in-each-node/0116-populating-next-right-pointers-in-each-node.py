"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, dummy: 'Optional[Node]') -> 'Optional[Node]':
        res = []
        level = 1
        root = dummy
        self.dfs(root, res, level)
        for arr in res:
            for i in range(len(arr)):
                if i==len(arr)-1:
                    arr[i].next = None
                else:
                    arr[i].next = arr[i+1]
        
        return dummy
        
    
    def dfs(self, root, res, level):
        if root is None:
            return
        
        if level>len(res):
            res.append([root])
        else:
            res[level-1] += [root]
        
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)