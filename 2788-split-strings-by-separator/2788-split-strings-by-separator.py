class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for word in words:
            lis = word.split(separator)
            while True:
                if "" in lis:
                    lis.remove("")
                else:
                    break
            res += lis
      
        return res