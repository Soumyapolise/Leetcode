class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        vals = sum(d.values())
        res = 0
        cumulative_sum = 0 
        
        for val in d.values():
            cumulative_sum += val
            res += (vals - cumulative_sum)
         
        return res
        
            
            