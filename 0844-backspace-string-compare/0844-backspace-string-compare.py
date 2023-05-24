class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.build(s) == self.build(t)
    
    def build(self, text):
        stack = []
        for ch in text:
            if ch == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)