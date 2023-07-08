class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[0:k])
        
        i = 1
        j = k
        res = sums/k
        while j<len(nums):
            sums -= nums[i-1]
            sums += nums[j]
            
            res = max(res, sums/k)
            i+=1 
            j+=1
        
        return res
            