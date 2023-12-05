class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        max_index = 0
        n = len(s)
        
        for i in range(n):
            right = i
            
            while right < n and s[i] == s[right]:
                right += 1
            
            #caaac
            
            left = i - 1
            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            curr_length = right - left - 1
            
            if curr_length > max_length:
                max_length = curr_length
                max_index = left + 1
            
        
        return s[max_index:max_index + max_length]
            