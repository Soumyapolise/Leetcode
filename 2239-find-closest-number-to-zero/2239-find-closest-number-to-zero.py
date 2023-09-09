class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff = float('inf')
        res = float('-inf')
        
        for num in nums:
            if abs(num) < diff:
                diff = abs(num)
                res = num
            elif abs(num) == diff:
                res = max(res, num)
        
        return res
            
            
            