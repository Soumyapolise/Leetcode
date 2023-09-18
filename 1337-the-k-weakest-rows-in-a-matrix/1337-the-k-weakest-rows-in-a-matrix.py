class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in range(len(mat)):
            c = mat[i].count(1)
            if c not in d:
                d[c] = []
            d[c] += [i]
        
        res = []
        
        for key in sorted(d.keys()):
            res += d[key]
            
        return res[:k]
        
        