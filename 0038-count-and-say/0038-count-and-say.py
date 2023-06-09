class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def calculate(i, s):
            if i == n+1:
                return s
            count = 0
            j = 0
            res = ""
            while j<len(s):
                ch = s[j]
                count = 1
                while j<len(s)-1 and s[j] == s[j+1]:
                    count+=1
                    j += 1
                res += str(count) + s[j]
                j+=1
            return calculate(i+1, res)
        
        return calculate(2, "1")
        
        