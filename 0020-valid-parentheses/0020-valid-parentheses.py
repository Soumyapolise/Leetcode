class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", "}":"{", "]":"["}
        
        stack = []
        o = 0
        for ch in s:
            if ch in d:
                if o == 0 or stack[-1] != d[ch]:
                    return False
                else:
                    stack.pop()
                    o -= 1
            else:
                o += 1
                stack.append(ch)
        
        return o == 0