class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}
        res = []
        
        for name in names:
            if name not in d:
                res.append(name)
                d[name] = 1 #suffix
            else:
                val = name + "(" + str(d[name]) + ")"
                k = 1
                while val in d:
                    val = name + "(" + str(d[name] + k) + ")"
                    k += 1
                d[name] = k
                d[val] = 1
                res.append(val)
        
        return res