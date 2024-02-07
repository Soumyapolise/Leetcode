class Solution:
    def frequencySort(self, s: str) -> str:
        s = sorted(s)
        d_count = {}
        for ch in s:
            if ch not in d_count:
                d_count[ch] = 0
            d_count[ch] += 1
        
        d_chars = {}
        for key, val in d_count.items():
            if val not in d_chars:
                d_chars[val] = []
            
            d_chars[val] += [key]
            
        
        res = ""
        
        k = sorted(d_chars.keys())[::-1]
        for c in k:
            for ch in d_chars[c]:
                res += ch*c
        
        return res