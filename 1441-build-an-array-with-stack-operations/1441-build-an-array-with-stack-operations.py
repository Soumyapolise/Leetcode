class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = ["Push"]*(target[-1])
        
        j = 0
        carry = 0
        for i in range(1, n+1):
            if i == target[j]:
                j += 1
            else:
                res = res[0:i+carry] + ["Pop"] + res[i+carry:]
                carry += 1
                
            if j == len(target):
                return res
        
        return res
                
            