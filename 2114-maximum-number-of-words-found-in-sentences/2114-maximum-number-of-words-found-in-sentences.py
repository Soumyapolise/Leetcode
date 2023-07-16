class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res = 0
        for s in sentences:
            currLength = len(s.split(" "))
            res = max(res, currLength)
        
        return res