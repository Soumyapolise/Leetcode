class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        i = 0
        j = len(nums) - 1
        for p in range(len(nums)-1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[p] = nums[i]*nums[i]
                i+=1
            else:
                res[p] = nums[j]*nums[j]
                j-=1
        return res