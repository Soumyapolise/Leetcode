class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        count = 0
        
        while j >= 0 and nums[j] >= k:
            j -= 1
        
        nums = nums[0:j+1]
        
        while i<len(nums) and j>=0 and i<j:
            n = len(nums)-1
            if nums[i] + nums[j] == k:
                #print(nums, i, j)
                count += 1
                i += 1
                j -= 1
                
                # print(nums)
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        
        return count
        
        
            