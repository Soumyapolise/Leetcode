class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        d = {}
        for num in nums:
            for n in num:
                if n in d:
                    d[n] += 1
                else:
                    d[n] = 1
        
        l = len(nums)
        res = []
        
        for key, val in d.items():
            if val == l:
                res.append(key)
        
        return sorted(res)
                