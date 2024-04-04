class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        res = count = 0
        
        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")":
                count -= 1
                
            res = max(res, count)
        
        return res