class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and k and stack[-1] > n:
                stack.pop()
                k -= 1
            
            if stack:
                stack.append(n)
            else:
                if n != "0":
                    stack.append(n)
            
        
        if k > 0:
            stack = stack[0:-k]
        
        if not stack:
            return "0"
        
        return "".join(stack)