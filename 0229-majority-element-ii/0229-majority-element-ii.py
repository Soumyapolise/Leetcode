class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         if n < 3:
#             return list(set(nums))
        
#         d = {}
#         for num in nums:
#             if num not in d:
#                 d[num] = 0
#             d[num] += 1
        
#         res = []
#         count = n//3
#         for key, val in d.items():
#             if val > count:
#                 res.append(key)
        
#         return res

        candidate1, candidate2, count1, count2 = None, None, 0, 0
        for num in nums:
            if candidate1 is not None and num == candidate1:
                count1 += 1
            elif candidate2 is not None and num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        count = len(nums)//3
        if nums.count(candidate1) > count:
            res.append(candidate1)
        
        if nums.count(candidate2) > count:
            res.append(candidate2)
        
        return res