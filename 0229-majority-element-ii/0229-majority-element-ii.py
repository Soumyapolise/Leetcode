class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 3:
            return list(set(nums))
        
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        res = []
        count = n//3
        for key, val in d.items():
            if val > count:
                res.append(key)
        
        return res