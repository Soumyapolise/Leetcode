class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        vals = list(d.values())
        vals = sorted(vals)[::-1]
        
        i = 0
        res = []
        for num in d.keys():
            if d[num] >=vals[k-1]:
                res.append(num)
        return res