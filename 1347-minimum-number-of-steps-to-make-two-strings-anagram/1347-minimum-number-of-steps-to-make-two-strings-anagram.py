class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d = {}
        
        for ch in s:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        
        for ch in t:
            if ch in d:
                if d[ch] > 0:
                    d[ch] -= 1
        
        return sum(d.values())