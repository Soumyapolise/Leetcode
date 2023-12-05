class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        for i in range(n):
            #checking for occurrence of the same character as s[i], consecutively
            right = i
            while right < n and s[i] == s[right]:
                right += 1
                res += 1
            
            #checking for side by side letters, if they are same - XaaaX
            
            left = i-1 
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                #print(s[left+1:right])
                res += 1
        
        return res