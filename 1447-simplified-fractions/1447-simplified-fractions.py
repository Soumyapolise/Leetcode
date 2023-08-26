from fractions import Fraction
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        den = []
        
        for num in range(2, n+1):
            den.append(num)
        
        for num in den:
            for i in range(1, num):
                res.append(str(Fraction(i, num)))
        
        return list(set(res))
        