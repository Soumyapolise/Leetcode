class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = n2 = 0
        
        for ch in num1:
            n1 = n1*10 + int(ch)
        
        for ch in num2:
            n2 = n2*10 + int(ch)
        
        res = n1*n2
        
        return str(res)
        