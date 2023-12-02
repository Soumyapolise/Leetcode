class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        for ch in chars:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
        res = 0
        
        for word in words:
            d1 = d.copy()
            forms = True
            for ch in word:
                if ch in d1:
                    if d1[ch] == 0:
                        forms = False
                        break
                    d1[ch] -= 1
                else:
                    forms = False
            
            if forms:
                res += len(word)
            
        return res