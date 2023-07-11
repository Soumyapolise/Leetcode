class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        zeroCount = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                if nums[i] == 0:
                    zeroCount -= 1
                i += 1
            res = max(res, j-i+1)
        
        return res-1