class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = -1
        maxi = -1
        for i in range(len(divisors)):
            x = divisors[i]
            count = 0
            for j in range(len(nums)):
                y = nums[j]
                if y % x == 0:
                    count +=1
            if count > maxi:
                maxi = count
                res = x
            elif count == maxi:
                res = min(res, x)
        
        return res
        