class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(len(s)):
            right = i
            while right < n and s[i] == s[right]:
                right += 1
                res += 1
            
            left = i-1
            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
        
        return res
            
            