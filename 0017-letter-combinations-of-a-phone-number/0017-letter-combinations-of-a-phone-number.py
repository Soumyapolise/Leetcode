class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        res = []
        if digits == "":
            return res
        
        self.dfs(digits, 0, "", res, d)
        
        return res
    
    def dfs(self, digits, index, string, res, d):
        if index == len(digits):
            res.append(string)
            return
        
        for ch in d[digits[index]]:
            self.dfs(digits, index + 1, string + ch, res, d)
        