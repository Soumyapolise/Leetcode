class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        
        for ch in t:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        
        left = 0
        missing_chars = len(d)
        min_length = float('inf')
        min_window = ""
        
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]] -= 1
                if d[s[right]] == 0:
                    missing_chars -= 1
            
            while missing_chars == 0:
                l = right - left + 1 #current window length
                if l < min_length:
                    min_window = s[left: right+1]
                    min_length = l
                
                if s[left] in d:
                    d[s[left]] += 1
                    if d[s[left]] > 0:
                        missing_chars += 1
                
                left += 1
        
        return min_window