class Solution:
    def reverseWords(self, s: str) -> str:
        lis = s.split()
        
        i = len(lis)-1
        
        res = ""
        while i >= 0:
            res += lis[i] + " "
            i -= 1
        
        return res[:-1:]