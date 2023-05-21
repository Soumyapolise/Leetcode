class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_par(num, i, res):
            if num == '':
                if i == res:
                    return True
                else:
                    return False
            for j in range(1, len(num)+1):
                if is_par(num[j:], i, res + int(num[:j])):
                    return True
            
            return False
                
        substring_sum = 0    
        for i in range(1, n+1):
            square = i * i
            if is_par(str(square), i, 0):
                substring_sum += square
            
        return substring_sum