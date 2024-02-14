class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        i = 0
        j = 0
        for k in range(n):
            if k % 2 == 0:
                while i < n and nums[i] < 0:
                    i += 1
                res[k] = nums[i]
                i += 1
            else:
                while j < n and nums[j] > 0:
                    j += 1
                res[k] = nums[j]
                j += 1
        return res
#         p, n = 0, 1
#         i, j = 0, 0
            
#         length = len(nums)
#         while p < length and n < length:
#             while i < length and nums[i] < 0:
#                 i += 1
            
#             while j < length and nums[j] > 0:
#                 j += 1
                
#             if p < length and nums[p] < 0:
#                 nums[p], nums[j] = nums[j], nums[p]
            
#             if n < length and nums[n] > 0:
#                 nums[n], nums[i] = nums[i], nums[n]
                
#             p += 2
#             n += 2
            
#         return nums
