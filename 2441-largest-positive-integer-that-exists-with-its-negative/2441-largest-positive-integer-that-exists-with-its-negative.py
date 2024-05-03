class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        maxi = -1
        
        negs = set()
        
        for n in nums:
            if n < 0:
                negs.add(n)
                
        for n in nums:
            if -1*n in negs:
                maxi = max(maxi, n)
        
        return maxi