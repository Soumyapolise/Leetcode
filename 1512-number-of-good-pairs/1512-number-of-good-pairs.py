import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        res = 0
        for key, val in d.items():
            if val > 1:
                res += math.factorial(val) // (math.factorial(val-2) * 2)
        
        return res