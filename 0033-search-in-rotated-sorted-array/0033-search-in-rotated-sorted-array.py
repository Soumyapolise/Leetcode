class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        n = len(nums)
        i = 0
        j = n-1
        
        while i <= j:
            mid = i + (j-i)//2
            real_mid = (mid + pivot) % n
            
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        
        return -1