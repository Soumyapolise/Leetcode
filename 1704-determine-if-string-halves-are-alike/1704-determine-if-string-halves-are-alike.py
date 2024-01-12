class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        count = 0
        
        mid = len(s)//2
        for ch in s[0:mid]:
            if ch in vowels:
                count += 1
                
        for ch in s[mid:]:
            if ch in vowels:
                count -= 1
        
        return count == 0