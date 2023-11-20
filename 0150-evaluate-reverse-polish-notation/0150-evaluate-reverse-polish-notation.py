class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+', '-', '*', '/'}
        
        for ch in tokens:
            if ch not in op:
                stack.append(ch)
            else:
                y = int(stack.pop())
                x = int(stack.pop())
                if ch == "+":
                    stack.append(str(x+y))
                elif ch == "-":
                    stack.append(str(x-y))
                elif ch == "*":
                    stack.append(str(x*y))
                else:
                    val = x/y
                    if val < 0:
                        val = math.ceil(val)
                    else:
                        val = x//y
                    stack.append(str(val))
            
        return int(stack.pop())
                