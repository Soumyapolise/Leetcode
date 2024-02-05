class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                d[s[i]] = "#"
        
        for val in d.values():
            if val != "#":
                return val
        
        return -1