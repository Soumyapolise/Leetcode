class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[1])
        
        k = float('-inf')
        res = 0
        
        for interval in intervals:
            if interval[0] >= k:
                k = interval[1]
            else:
                res += 1
            
        return res