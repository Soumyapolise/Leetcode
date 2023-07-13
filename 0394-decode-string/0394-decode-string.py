class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        num = 0
        
        for ch in s:
            if ch.isnumeric():
                num = num*10 + int(ch)
            elif ch == "[":
                stack.append(res)
                stack.append(num)
                res = ""
                num = 0
            elif ch == "]":
                count = stack.pop()
                prev_string = stack.pop()
                
                res = prev_string + count*res
            else:
                res += ch
        
        return res
                