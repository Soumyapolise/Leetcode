class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        
        for i in range(n):
            right = i
            while right < n and s[right] == s[i]:
                right += 1
                res += 1
            
            left = i - 1
            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1
        
        return res
            