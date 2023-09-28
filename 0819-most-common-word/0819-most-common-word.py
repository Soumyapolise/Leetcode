import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        x = paragraph.lower()
        p = re.split('[ !?'',;.]', x)
        i = 0
        while i < len(p):
            r = ""
            if p[i] == "":
                p = p[0:i] + p[i+1:]
                continue
            for ch in p[i]:
                if ch.isalpha():
                    r += ch
            
            p = p[0:i] + [r] + p[i+1:]
            i += 1
        d = {}
        for word in p:
            if word not in d:
                d[word] = 0
            
            if word not in banned:
                d[word] += 1
        
        maxi = float('-inf')
        res = ""
        for key, val in d.items():
            if val > maxi:
                res = key
                maxi = val
        
        return res
            