class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = -1
        maxi = -1
        for i in range(len(divisors)):
            count = 0
            for j in range(len(nums)):
                if nums[j]%divisors[i] == 0:
                    count +=1
            if count > maxi:
                maxi = count
                res = divisors[i]
            elif count == maxi:
                res = min(res, divisors[i])
        
        return res
        