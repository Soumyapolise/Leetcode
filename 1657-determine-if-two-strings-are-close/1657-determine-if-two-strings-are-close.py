class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # word1.sort()
        # word2.sort()
        
        if len(word1) != len(word2):
            return False
        d2 = {}
        d = {}
        for ch in word1:
            if ch not in d:
                d[ch] = 0
            d[ch] += 1
            
        for ch in word2:
            if ch not in d2:
                d2[ch] = 0
            
            d2[ch] += 1
        
        return sorted(d.keys()) == sorted(d2.keys()) and sorted(d.values()) == sorted(d2.values()) ##as long as the keys are same and values (doesn't have to respected to keys mentioned before) are same as well - we can just swap them around to achieve the same strings.
        