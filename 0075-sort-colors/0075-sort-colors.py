class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        
        while i<j:
            if nums[i] in [1,2] and nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            elif nums[i] == 0:
                i+=1
            else:
                j-=1
        
        j = len(nums)-1
        while i<j:
            if nums[i] == 2:
                if nums[j] == 1:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    j-=1
            else:
                i+=1
            
        
            
        