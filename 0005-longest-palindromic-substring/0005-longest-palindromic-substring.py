class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            return right - left - 1
        
        res = [0, 0]
        
        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > res[1] - res[0] + 1:
                dist = odd_length // 2
                res = [i - dist, i + dist]
            
            even_length = expand(i, i+1)
            if even_length > res[1] - res[0] + 1:
                dist = (even_length // 2) - 1
                res = [i - dist, i + 1 + dist]
            
        i, j = res
        return s[i:j+1]