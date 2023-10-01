class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        s = s.split()
        while i < len(s):
            stack = []
            for ch in s[i]:
                stack.append(ch)
            res = ""
            while stack:
                res += stack.pop()
            
            s = s[0:i] + [res] + s[i+1:]
            i += 1
            
        return " ".join(s)