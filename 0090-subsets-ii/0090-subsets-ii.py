class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums = sorted(nums)
        
        for num in nums:
            for i in range(len(res)):
                res.append(res[i] + [num])
        
        d = {}
        for arr in res:
            d[tuple(arr)] = 1
        
        return list(d.keys())