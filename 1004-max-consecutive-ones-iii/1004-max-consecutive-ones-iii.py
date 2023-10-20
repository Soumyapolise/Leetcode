class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = float('-inf')
        left = 0
        zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                
            res = max(res, right - left + 1)
        
        return res