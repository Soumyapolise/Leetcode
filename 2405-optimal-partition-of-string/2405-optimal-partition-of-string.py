class Solution:
    def partitionString(self, s: str) -> int:
        res = []
        substring = ""
        for ch in s:
            if ch in substring:
                res.append(substring)
                substring = ""
            substring += ch
        
        if substring != "":
            res.append(substring)
            
        return len(res)