class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        
        for i in range(len(groupSizes)):
            if groupSizes[i] in d:
                d[groupSizes[i]] += [i]
            else:
                d[groupSizes[i]] = [i]
                
        res = []
        for size, item in d.items():
            if len(item) > size:
                k = len(item)//size
                for i in range(k):
                    res.append(item[i:i+size])
            else:
                res.append(item)
        
        return res