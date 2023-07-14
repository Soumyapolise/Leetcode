class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        res = 0
        
        for num in arr:
            if num-difference in d:
                count = d[num-difference]
            else:
                count = 0
            
            d[num] = count + 1
            
            res = max(res, d[num])
        
        return res