import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        
        high = max(nums)
        
        while low <= high:
            res = 0
            mid = low + (high-low)//2
            
            for num in nums:
                res += math.ceil(num/mid)
            
            if res > threshold:
                low = mid + 1
            else:
                high = mid-1
        
        return low