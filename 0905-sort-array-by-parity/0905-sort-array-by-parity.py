class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n-1
        if n == 1:
            return nums
        
        while i < j:
            while j >= 0 and nums[j]%2 != 0:
                j -= 1
            while i < n and nums[i]%2 == 0:
                i += 1
            if i == n or j == -1 or i > j:
                return nums
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return nums
        