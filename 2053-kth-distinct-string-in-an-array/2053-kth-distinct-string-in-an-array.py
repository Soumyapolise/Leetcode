class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = {}
        lis = []
        for ch in arr:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        
        for key, value in d.items():
            if value == 1:
                k -= 1
                
            if k == 0:
                return key
        
        return ""
        