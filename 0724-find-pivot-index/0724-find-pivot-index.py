class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums) - nums[0]
        
        for i in range(len(nums)):
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            if i == len(nums)-1:
                rightSum = 0
            else:
                rightSum -= nums[i+1]
            
        return -1
        