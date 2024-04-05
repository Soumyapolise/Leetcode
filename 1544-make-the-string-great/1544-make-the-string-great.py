class Solution:
    def makeGood(self, s: str) -> str:
        n = len(s)
        
        def upperCount(s):
            count = 0
            for ch in s:
                if ch.isupper():
                    count += 1
            
            return count
        
        i = 0
        if upperCount(s) == 0:
            return s
        while upperCount(s) > 0 and (i == 0 or len(s) != n):
            n = len(s)
            stack = []
            i = 1
            for ch in s:
                if not stack:
                    stack.append(ch)
                elif ch.lower() == stack[-1].lower() and ch != stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
            
            s = "".join(stack)
        
        
        return "".join(stack)