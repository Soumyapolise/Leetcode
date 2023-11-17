class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0
        
        mini = min(nums)
        res = 0
        
        for num in nums:
            res += num - mini
        
        return res