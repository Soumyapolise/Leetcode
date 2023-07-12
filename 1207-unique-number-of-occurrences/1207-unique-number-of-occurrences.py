class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        return len(set(d.values())) == len(d.values())