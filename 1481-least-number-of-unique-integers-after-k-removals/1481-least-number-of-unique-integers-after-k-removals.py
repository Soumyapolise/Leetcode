class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 0
                
            d[num] += 1
        
        counts = sorted(list(d.values()))
        
        n = len(counts)
        for i in range(n):
            k -= counts[i]
            if k < 0:
                return n - i
            elif k == 0:
                return n - i - 1