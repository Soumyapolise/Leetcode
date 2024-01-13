class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = 0
        self.dfs([], res, nums)
        return res
    
    def dfs(self, curr, res, nums):
        if len(curr) == len(nums):
            res.append(curr)
            return
        
        for n in nums:
            if n not in curr:
                self.dfs(curr + [n], res, nums)
                