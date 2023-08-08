class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #finding pivot first
        pivot = nums.index(min(nums))
        
        n = len(nums)
        # nums = nums[pivot:n] + nums[0:pivot]
        l = 0
        r = n - 1
        
        while l <= r:
            mid = l + (r-l)//2
            real_mid = (mid + pivot)%n
            if nums[real_mid] == target:
                return real_mid
            
            if nums[real_mid] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return -1