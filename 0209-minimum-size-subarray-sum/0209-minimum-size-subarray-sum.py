class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        
        if target in nums:
            return 1
        
        i, j = 0, 0
        res = 0
        sums = nums[0]
        while i<=j and j<len(nums):
            
            if sums<target:
                j+=1
                if j>=len(nums):
                    break
                sums += nums[j]
            elif sums>target:
                if res!=0:
                    res = min(res, j-i+1)
                else:
                    res = j-i+1
                sums -= nums[i]
                i+=1
            else:
                if res!=0:
                    res = min(res, j-i+1)
                else:
                    res = j-i+1
                j+=1
                if j>=len(nums):
                    break
                sums += nums[j]
        
        return res
                