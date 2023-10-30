class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        
        for num in arr:
            val = bin(num).count("1")
            if val not in d:
                d[val] = []
            d[val] += [num]
        
        res = []
        keys = sorted(d)
        for key in keys:
            res += sorted(d[key])
        
        return res