class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res = []
        self.dfs(digits, 0, d, res, "")
        return res
        
    def dfs(self, digits, i, d, res, ch):
        if len(ch) == len(digits):
            res.append(ch)
            return
        
        for x in d[digits[i]]:
            self.dfs(digits, i+1, d, res, ch+x)
        
        