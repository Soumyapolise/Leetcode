class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in range(len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] == -asteroids[i]:
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(asteroids[i]):
                    break
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                    continue
            else:
                stack.append(asteroids[i])
        
        return stack
        