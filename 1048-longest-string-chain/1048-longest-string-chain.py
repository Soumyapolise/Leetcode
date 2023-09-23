class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len) #sorting the words by their length
        
        res = 1
        d = {}
        
        for word in words:
            d[word] = 1 #updating by minimum occurrence
            
            for i in range(len(word)):
                p = word[:i] + word[i+1:] #checking without the i'th letter for predecessor -> if it's in d
                if p in d: #if predecessor already in d, update d[word] with whatever is max as done below:
                    d[word] = max(d[word], d[p] + 1)
            
            res = max(res, d[word]) #just updating res as we go for max value
        
        return res