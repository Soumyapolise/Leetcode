class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            
        d = dict(sorted(d.items(), key = lambda x:x[1], reverse=True))
        max_char = list(d.keys())[0]
        max_count = list(d.values())[0]
        
        if max_count > (len(s)+1)//2:
            return ""
        
        res = [max_char]*max_count
        i = 0
        for key, value in d.items():
            if key == max_char:
                continue
            for _ in range(value):
                res[i] += key
                i+=1
                if i == len(res):
                    i = 0
        
        return "".join(res)