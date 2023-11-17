class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        i = 0
        j = len(nums)-1
        
        maxi = float('-inf')
        
        while i < j:
            maxi = max(maxi, nums[i] + nums[j])
            i += 1
            j -= 1
        
        return maxi