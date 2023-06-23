class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {}
        
        for right in range(len(nums)):
            for left in range(0, right):
                diff = nums[right]-nums[left]
                if (left, diff) in d:
                    d[(right, diff)] = d[(left, diff)] + 1
                else:
                    d[(right, diff)] = 2
        
        return max(d.values())