class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        j = len(nums)-1
        count = 0
        
        #getting rid of elements that are greater or equal to k from the right of the array
        while j >= 0 and nums[j] >= k: 
            j -= 1 
        
        
        while i<j:
            if nums[i] + nums[j] == k:
                count += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        
        return count
        
        
            