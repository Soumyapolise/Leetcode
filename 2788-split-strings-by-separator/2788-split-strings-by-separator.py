class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            lis = word.split(separator)
            
            res += lis
        
        i = 0
        
        while i < len(res):
            if res[i] == "":
                res = res[0:i] + res[i+1:]
            else:
                i += 1
                
        return res