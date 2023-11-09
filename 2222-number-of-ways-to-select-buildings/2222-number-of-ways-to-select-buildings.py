class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {"0": 0, "1": 0, "01": 0, "10": 0, "010": 0, "101": 0}
        
        for ch in s:
            if ch == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            else:
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]
        
        return dp["010"] + dp["101"]
    
    #only two subsequence possible, 010 and 101, now we'll try to simulate the process of making them. As we traverse the string, we look if it's 0 or 1, accordingly, we'll update our dp["0"] and dp["1"], along witb that, we'll update our 10 and 01 strings respectively, meaning that, if we had encountered a "1" already before "0" came along, we can make "10" string with that, so when we encounter "0" (essentially looking for substrings ending with "0"), we add dp["1"] to dp["10"] and so on. Similarly for dp["010"], when we encounter "0" (again, looking for substring ending with "0"), we'll add dp["01"] to dp["010"]. 
            