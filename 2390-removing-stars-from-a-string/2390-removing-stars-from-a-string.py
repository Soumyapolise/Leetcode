class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(x for x in stack)