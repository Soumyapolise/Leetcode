class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        
        new_nums = sorted(set(nums))
        l = len(new_nums)
        j = 0
        
        for i in range(l):
            while j < l and new_nums[j] < new_nums[i] + n:
                j += 1
            
            count = j - i
            res = min(res, n - count)
        
        return res