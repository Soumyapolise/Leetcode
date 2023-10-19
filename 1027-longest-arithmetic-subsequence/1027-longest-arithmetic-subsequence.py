class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {}
        
        for right in range(1, len(nums)):
            for left in range(right):
                diff = nums[right] - nums[left]
                
                if (left, diff) in d:
                    d[(right, diff)] = d[(left, diff)] + 1
                else:
                    d[(right, diff)] = 2
        
        return max(d.values())