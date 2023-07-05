class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        l = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        while i<j:
            while i<len(s) and s[i] not in l:
                i += 1
                
            while j>=0 and s[j] not in l:
                j -= 1
            
            if i<j:
                s = s[0:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                i += 1
                j -= 1
            else:
                return s
        
        return s
        