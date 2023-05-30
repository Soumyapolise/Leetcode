class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        
        count = 0
        prod = 1
        i = 0
        
        for j in range(len(nums)):
            prod *= nums[j]
            while prod >= k:
                prod = prod//nums[i]
                i += 1
            
            count += j - i + 1
        
        return count
        