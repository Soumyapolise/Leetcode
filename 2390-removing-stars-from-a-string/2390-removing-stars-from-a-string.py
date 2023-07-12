class Solution:
    def removeStars(self, s: str) -> str:
#         stack = []
#         for ch in s:
#             if ch == "*":
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(ch)
        
#         return "".join(x for x in stack)
        stack = []
        i = 0
        
        while i < len(s):
            if s[i] == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
            i += 1
        
        return "".join(x for x in stack)