class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, third = [], float('-inf')
        
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
            
        return False
    
#         stack = []
#         rev = True
        
#         for n in nums:
#             # print(stack)
#             if not stack:
#                 stack.append(n)
#                 continue
            
#             if (rev and n <= stack[-1]) or (n >= stack[-1] and not rev):
#                 stack.pop()
#                 stack.append(n)
#             else:
#                 stack.append(n)
#                 rev = False
            
#             if len(stack) == 3:
#                 if stack[-1] <= stack[0]:
#                     stack.pop()
#                     continue
#                 return True
        
#         return False
            
            