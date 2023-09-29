class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:0}
        
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            
            if sums % k not in d:
                d[sums % k] = i + 1
            elif d[sums % k] < i:
                return True
        
        return False