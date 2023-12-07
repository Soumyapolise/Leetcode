class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            res = max(res, heights[i])
            idx = i
            while stack and stack[-1][0] > heights[i]:
                idx = stack[-1][1]
                res = max(res, stack[-1][0]*(i - idx))
                stack.pop()
            stack.append([heights[i], idx])
            
            
        for h, i in stack:
            res = max(res, h * (len(heights) - i))
            i += 1
                
            
            
        return res