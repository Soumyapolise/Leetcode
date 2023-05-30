class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = {}
        for i in range(len(nums)):
            target = nums[i]*(-1)
            d = {}
            for j in range(i+1, len(nums)):
                if nums[j] in d:
                    res[tuple(sorted([nums[j], d[nums[j]], nums[i]]))] = 1
                else:
                    d[target-nums[j]] = nums[j]
        
        return res.keys()