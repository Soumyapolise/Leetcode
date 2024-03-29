class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = False
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc = True
            elif nums[i] < nums[i-1]:
                dec = True
                
            if inc and dec:
                return False
            
        return True
#         if len(nums) == 1 or len(nums) == 2:
#             return True
        
#         diff = nums[-1] - nums[0]
#         if diff == 0:
#             if len(set(nums)) == 1:
#                 return True
#             else:
#                 return False
            
#         for i in range(1, len(nums)):
#             val = nums[i] - nums[i-1]
#             if (val <= 0 and diff < 0) or (val >= 0 and diff > 0):
#                 continue
#             else:
#                 return False
        
#         return True
                