class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
                
            d[num] += 1
        
        val = max(d.values())
        
        return list(d.values()).count(val) * val
                