class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 1
        #[1,3,0,0,12]
        while j<len(nums):
            if i<len(nums) and nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                # j += 1
            else:
                i += 1
            j += 1
                
            
                 
        