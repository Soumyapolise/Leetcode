class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures)-1, -1, -1):
            count = 0
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
                
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1] - i)
            stack.append(i) 
            
        return res[::-1]