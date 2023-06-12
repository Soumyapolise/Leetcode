class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current = []
        nums.sort()  # Sort the array to handle duplicates
        self.backtrack(0, current, subsets, nums)
        return subsets

    def backtrack(self, startIndex, current, subsets, nums):
        subsets.append(current[:])  # Add the current subset to the subsets list

        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i-1]:
                continue

            current.append(nums[i])  # Add the current element to the current subset
            self.backtrack(i + 1, current, subsets, nums)  # Recursively call backtrack
            current.pop()  # Remove the current element (backtrack)

        
#         res = [[]]
#         nums = sorted(nums)
        
#         for num in nums:
#             for i in range(len(res)):
#                 res.append(res[i] + [num])
        
#         d = {}
#         for arr in res:
#             d[tuple(arr)] = 1
        
#         return list(d.keys())