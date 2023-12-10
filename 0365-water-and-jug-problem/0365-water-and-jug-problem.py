class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        if jug1 + jug2 < target:
            return False
        
        if target % gcd(jug1, jug2) != 0:
            return False
        
        return True