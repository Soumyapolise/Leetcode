class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        s = s.split()
        while i < len(s):
            s = s[0:i] + [s[i][::-1]] + s[i+1:]
            i += 1
            
        return " ".join(s)