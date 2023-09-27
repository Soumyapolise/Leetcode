class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self.dfs(nums, 0, memo)

    def dfs(self, nums, i, memo):
        # If we have reached or exceeded the end of the array, return 0
        if i >= len(nums):
            return 0

        # If the result for this index is already computed, return it
        if i in memo:
            return memo[i]

        # Calculate the maximum amount that can be robbed starting from this house
        # We have two choices: rob this house and move two steps ahead, or skip this house and move one step ahead
        max_amount = max(nums[i] + self.dfs(nums, i + 2, memo), self.dfs(nums, i + 1, memo))

        # Store the result in the memo table
        memo[i] = max_amount

        return max_amount
        
#         lis = []
#         res = 0
#         memo = {}
#         for i in range(len(nums)):
#             res = 0
#             self.dfs(nums, i, res, lis)
        
#         return max(lis)
        
        
#     def dfs(self, nums, i, res, lis):
#         if i >= len(nums):
#             return
        
        
#         if i == len(nums)-1 or i == len(nums)-2:
#             lis.append(res + nums[i])
#             return
        
#         idx = []
#         start = i
#         while start < len(nums):
#             if start != i and start != (i+1):
#                 idx.append(start)
#             start += 1
        
#         if idx == []:
#             lis.append(res + nums[i])
#             return
        
#         for j in idx:
#             self.dfs(nums, j, res + nums[i], lis)
        
        
        