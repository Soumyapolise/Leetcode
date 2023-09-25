class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        
        for ch in s:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        
        for ch in t:
            if ch not in d:
                return ch
            elif d[ch] == 0:
                return ch
            
            d[ch] -= 1
        
        