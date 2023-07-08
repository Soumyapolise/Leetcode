class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        
        for ch in s[0:k]:
            if ch in vowels:
                count += 1
        
        res = count
        i, j = 1, k
        
        while j<len(s):
            if s[j] in vowels:
                count += 1
            if s[i-1] in vowels:
                count -= 1
            
            res = max(res, count)
            i += 1
            j += 1
        
        return res
        
                