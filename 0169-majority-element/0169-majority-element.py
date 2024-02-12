class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
            
            if d[num] > n:
                return num