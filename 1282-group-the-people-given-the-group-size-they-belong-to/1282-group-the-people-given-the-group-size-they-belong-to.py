class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        res = []
        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                d[groupSizes[i]] = []
                
            d[groupSizes[i]] += [i]
            
            if len(d[groupSizes[i]]) == groupSizes[i]:
                res.append(d[groupSizes[i]])
                d[groupSizes[i]] = []
        
        return res

            