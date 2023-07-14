class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = {}
        res = 0
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        for key, val in d.items():
            if val == 1:
                res += key
        
        return res