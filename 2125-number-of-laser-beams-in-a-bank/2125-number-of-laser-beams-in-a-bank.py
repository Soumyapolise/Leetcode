class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        
        for i in range(len(bank)):
            count = 0
            count = bank[i].count("1") #adding levels that has devices to seen 
            
            if count != 0:
                res += prev * count
                prev = count
        
        return res
            
            
                
        