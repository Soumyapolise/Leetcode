class Solution:
    def bestClosingTime(self, customers: str) -> int:
        p = 0
        
        for i in range(len(customers)):
            if customers[i] == "Y":
                p += 1
                
        p_val = p
        res = 0
        for j in range(1, len(customers)+1):
            if customers[j-1] == "Y":
                p -= 1
            else:
                p += 1
            
            if p < p_val:
                p_val = p
                res = j
        
        return res
            
        