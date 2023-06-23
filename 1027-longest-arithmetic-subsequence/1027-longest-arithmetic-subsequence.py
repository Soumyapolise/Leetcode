class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {}
        
        for right in range(len(nums)):
            for left in range(0, right):
                if (left, nums[right]-nums[left]) in d:
                    d[(right, nums[right]-nums[left])] = d[(left, nums[right]-nums[left])] + 1
                else:
                    d[(right, nums[right]-nums[left])] = 2
        
        return max(d.values())