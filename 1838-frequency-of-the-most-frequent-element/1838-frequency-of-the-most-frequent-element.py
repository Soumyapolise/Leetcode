class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        res = 0
        curr = 0
        
        for right in range(len(nums)):
            target = nums[right]
            curr += target
            
            while (right - left + 1)*target-curr > k:
                curr -= nums[left]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res