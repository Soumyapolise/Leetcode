class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "]":"[", "}":"{"}
        stack = []
        
        for ch in s:
            if ch not in d:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack[-1] != d[ch]:
                    return False
                stack.pop()
                
        return stack == []