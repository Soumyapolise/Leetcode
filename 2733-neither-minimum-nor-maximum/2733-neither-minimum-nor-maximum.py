import random
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return -1
        
        maxi = max(nums)
        mini = min(nums)
        n = maxi
        while n == maxi or n == mini:
            n = random.choice(nums)
       
        return n