class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1: return 0
        pro = 1
        cnt = 0 
        j = 0 
        for i in range(len(nums)):
            pro *= nums[i]
            while pro >= k: 
                pro //= nums[j]
                j += 1 
            cnt += i - j + 1 
        return cnt