class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = sorted(p)
        len_p = len(p)
        res = []
        
        for i in range(len(s)-len_p+1):
            if sorted(s[i:i+len_p]) == p:
                res.append(i)
        
        return res