class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
#         stack = [asteroids[0]]
#         if stack[0] > 0:
#             sign = "+"
#         else:
#             sign = "-"
            
#         def check(asteroids, sign):
#             for i in range(1, len(asteroids)):
#                 prev = sign
#                 if asteroids[i] > 0:
#                     sign = "+"
#                 else:
#                     sign = "-"

#                 if prev != sign:
#                     if abs(stack[-1]) < abs(asteroids[i]):
#                         stack.pop()
#                         stack.append(asteroids[i])
#                     elif abs(stack[-1]) == abs(asteroids[i]):
#                         stack.pop()
#                 else:
#                     stack.append(asteroids[i])
        
#         for num in 
#         check(asteroids, sign)
        
        
#         return stack
        res = []
        for asteroid in asteroids:
            while len(res) and asteroid < 0 and res[-1] > 0:
                if res[-1] == -asteroid: 
                    res.pop()
                    break
                elif res[-1] < -asteroid:
                    res.pop()
                    continue
                elif res[-1] > -asteroid:
                    break
            else:
                res.append(asteroid)
        return res