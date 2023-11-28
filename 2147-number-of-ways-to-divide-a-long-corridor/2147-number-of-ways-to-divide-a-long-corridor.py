class Solution:
    def numberOfWays(self, corridor: str) -> int:
        d = {"S": []}
        count = 0
        MOD = 10**9 + 7
        for i in range(len(corridor)):
            if corridor[i] == "S":
                count += 1
                d["S"] += [i]
        
        if count < 2 or count % 2 != 0:
            return 0
        if count == 2:
            return 1
        res = 1
        
        for i in range(1, len(d["S"])-1, 2):
            res *= (d["S"][i+1] - d["S"][i])%MOD
            res %= MOD
        return res%MOD
            
            
        
        
                    