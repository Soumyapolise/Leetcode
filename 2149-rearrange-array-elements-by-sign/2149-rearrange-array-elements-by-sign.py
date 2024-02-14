class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        pos = 0
        neg = 1
        for k in range(n):
            if nums[k] > 0:
                res[pos] = nums[k]
                pos += 2
            else:
                res[neg] = nums[k]
                neg += 2
        return res