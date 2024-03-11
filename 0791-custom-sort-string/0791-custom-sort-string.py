class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        
        for ch in s:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        
        res = ""
        
        for ch in order:
            if ch in d:
                res += ch*d[ch]
                d.pop(ch)
        
        for key, val in d.items():
            res += key*val
        
        return res