class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)*2
        
        for i in range(len(nums)):
            res[i] = res[i+len(nums)] = nums[i]
        
        return res