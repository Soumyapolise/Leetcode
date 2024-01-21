class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        sums = 0
        return self.dfs(0, nums, {})
        
        
    def dfs(self, i, nums, memo):
        if i >= len(nums):
            return 0
        
        if i in memo:
            return memo[i]
        
        memo[i] = max(nums[i] + self.dfs(i+2, nums, memo), self.dfs(i+1, nums, memo))
        
        return memo[i]