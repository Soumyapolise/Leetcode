class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        d = {"M":0, "P":0, "G":0}
        travel = [0] + travel
        d2 = {"M":0, "P":0, "G":0}
        for i in range(len(garbage)-1, -1, -1):
            set_ch = set(garbage[i])
            for ch in garbage[i]:
                d[ch] += 1
            
            if d2 == {"M":0, "P":0, "G":0}:
                for ch in set_ch:
                    d2[ch] += travel[i]
            else:
                seen = set()
                for key, val in d2.items():
                    if val > 0:
                        d2[key] += travel[i]
                        seen.add(key)
                
                for ch in set_ch:
                    if ch not in seen:
                        d2[ch] += travel[i]
        
        return sum(d.values()) + sum(d2.values())
            