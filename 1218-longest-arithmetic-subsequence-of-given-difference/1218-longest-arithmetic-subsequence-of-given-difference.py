class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        res = 0
        
        for i in range(len(arr)):
            if arr[i]-difference in d:
                count = d[arr[i]-difference]
            else:
                count = 0
            
            d[arr[i]] = count + 1
            
            # res = max(res, d[arr[i]])
        
        return max(d.values())