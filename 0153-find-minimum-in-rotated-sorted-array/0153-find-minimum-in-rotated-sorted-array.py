class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = n-1
        if len(nums) == 1:
            return nums[0]
        while i <= j:
            mid = (i + (j-i)//2)
            
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid] > nums[-1]:
                i = mid + 1
            else:
                j = mid - 1
                
            
        