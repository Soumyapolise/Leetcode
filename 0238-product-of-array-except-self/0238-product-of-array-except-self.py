class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        curr = 1
        for i in range(len(nums)):
            ans[i] *= curr
            curr *= nums[i]
        
        print(ans)
        curr = 1
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= curr
            curr *= nums[j] 
        
        return ans