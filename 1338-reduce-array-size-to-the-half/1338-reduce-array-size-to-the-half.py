class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        n = len(arr)
        n = n//2
        
        counts = list(d.values())
        counts.sort(reverse = True)
        
        sums = 0
        res = 0
        for c in counts:
            n -= c
            res += 1
            if n <= 0:
                return res
                