class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        
        return self.bSearch(low, high, nums)
    
    def bSearch(self, low, high, nums):
        if low == high:
            return low
        mid = low + (high-low)//2
        
        if nums[mid] > nums[mid+1]:
            return self.bSearch(low, mid, nums)
        
        return self.bSearch(mid+1, high, nums)