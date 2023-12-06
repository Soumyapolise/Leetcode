class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = n*2
        
        string = "("
        o = 1 #unpaired brackets
        res = []
        
        def dfs(string, o, res):
            if o > n or o < 0 or len(string) > l:
                return
            
            if len(string) == l:
                if o == 0:
                    res.append(string)
                return
            
            dfs(string + "(", o + 1, res)
            dfs(string + ")", o - 1, res)
            
        dfs(string, o, res)
        return res