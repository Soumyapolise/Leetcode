class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = 2*k + 1
        if len(nums) >= n:
            sums = sum(nums[0:n])
        else:
            return [-1]*len(nums)
        
        res = [-1]*(k)
            
        for i in range(k, len(nums)-k):
            res.append(sums//n)
            sums -= nums[i-k]
            if i < len(nums)-k-1:
                sums += nums[i+k+1]
        
        res += [-1]*(k)
        
        return res