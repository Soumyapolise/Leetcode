class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = 0
        right = 0
        s = ""
        res = []
        
        def dfs(left, right, s):
            if len(s) == n*2:
                res.append(s)
                return
            
            if left < n:
                dfs(left + 1, right, s + "(")
            
            if right < left:
                dfs(left, right + 1, s + ")")
        
        dfs(left, right, s)
        
        return res