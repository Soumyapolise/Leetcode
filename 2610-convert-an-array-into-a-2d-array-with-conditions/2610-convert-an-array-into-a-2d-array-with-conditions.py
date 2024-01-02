class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        res = []
        
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        while set(d.values()) != {0}:
            arr = []
            for key, val in d.items():
                if d[key] > 0:
                    arr.append(key)
                    d[key] -= 1
                
                
            res.append(arr)
        
        return res