class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        #divisors = divisors.set()
        d = {}
        for i in range(len(divisors)):
            count = 0
            for j in range(len(nums)):
                if nums[j]%divisors[i] == 0:
                    count +=1
            if count in d:
                d[count] += [divisors[i]]
            else:
                d[count] = [divisors[i]]
        
        maxi = max(d.keys())
        if len(d[maxi])>1:
            return min(d[maxi])
        else:
            return d[maxi][0]
        