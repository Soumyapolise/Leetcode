class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        
        for ch in s:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        
        for ch in t:
            if ch not in d:
                return False
            else:
                if d[ch] == 0:
                    return False
                d[ch] -= 1
        
        return set(d.values()) == {0}