class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff = float('inf')
        res = float('-inf')
        
        for num in nums:
            if num < 0:
                if num*(-1) < diff:
                    diff = num*(-1)
                    res = num
                elif num*(-1) == diff:
                    res = max(res, num)
                    diff = num*(-1)
            else:
                if num < diff:
                    res = num
                    diff = num
                elif num == diff:
                    res = max(res, num)
                    diff = num
            
        return res
            
            
            