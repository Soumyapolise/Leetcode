class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = -1
        mx_cnt = -1
        # for each divisor
        for d in divisors:
            cnt = 0
            # we check each number `x`
            for x in nums:
                # to see if `x` can be divisible by `d`
                if x % d == 0:
                    # if so, increase the counter by 1
                    cnt += 1
            # if the counter is greater than the current max
            if cnt > mx_cnt:
                # then update hte current max
                mx_cnt = cnt
                # `d` will be the possible answer
                res = d
            elif cnt == mx_cnt:
                # however, if the counter is same as the current max
                # then we need to take the min one
                res = min(res, d)
        return res
        
        
#         res = -1
#         maxi = -1
#         for i in range(len(divisors)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[j]%divisors[i] == 0:
#                     count +=1
#             if count > maxi:
#                 maxi = count
#                 res = divisors[i]
#             elif count == maxi:
#                 res = min(res, divisors[i])
        
#         return res
        