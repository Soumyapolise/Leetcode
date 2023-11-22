class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = {}
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                key = i + j
                if key not in d:
                    d[key] = []
                d[key] += [nums[i][j]]
        
        keys = sorted(d.keys())
        res = []
        for k in keys:
            res += d[k][::-1]
        
        return res