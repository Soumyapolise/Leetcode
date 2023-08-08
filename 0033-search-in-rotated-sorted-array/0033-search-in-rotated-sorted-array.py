class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #finding pivot first
        pivot = nums.index(min(nums))
        
        n = len(nums)
        nums = nums[pivot:n] + nums[0:pivot]
        print(nums)
        l = 0
        r = n - 1
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return (mid + pivot)%n
            
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return -1