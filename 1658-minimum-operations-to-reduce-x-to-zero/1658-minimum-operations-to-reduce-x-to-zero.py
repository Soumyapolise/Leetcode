class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x
        
        if target < 0:
            return -1
        
        max_length = -1
        i = 0
        sums = 0
        
        for j in range(n):
            sums += nums[j]
            
            while sums > target:
                sums -= nums[i]
                i += 1
            
            if sums == target:
                max_length = max(max_length, j - i + 1)
        
        if max_length != -1:
            return n - max_length
        else:
            return -1