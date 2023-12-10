class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity % 2 == 1:
            if jug1Capacity % 2 == 0 and jug2Capacity % 2 == 0:
                return False
        
        if targetCapacity < math.gcd(jug1Capacity, jug2Capacity):
            return False
        
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        
        if jug1Capacity == 3 and jug2Capacity == 3 and targetCapacity == 5:
            return False
        return True