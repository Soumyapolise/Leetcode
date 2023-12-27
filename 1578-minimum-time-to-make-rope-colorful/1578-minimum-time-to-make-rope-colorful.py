class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = []
        res = 0
        
        for i in range(len(colors)):
            if not stack:
                stack.append([colors[i], neededTime[i]])
            else:
                if stack[-1][0] == colors[i]:
                    if neededTime[i] > stack[-1][1]:
                        res += stack[-1][1]
                        stack.pop()
                        stack.append([colors[i], neededTime[i]])
                    else:
                        res += neededTime[i]
                else:
                    stack.append([colors[i], neededTime[i]])
        
        return res
        