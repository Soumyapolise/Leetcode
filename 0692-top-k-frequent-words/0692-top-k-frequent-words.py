class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        
        d = {}
        
        for w in words:
            if w not in d:
                d[w] = 0
            
            d[w] += 1
        
        vals = sorted(d.values())[::-1]
        res = []
        for i in range(len(vals)):
            for key, val in d.items():
                if val == vals[i]:
                    res.append(key)
                    d.pop(key)
                    break
            if len(res) >= k:
                break
        
        return res[0:k]