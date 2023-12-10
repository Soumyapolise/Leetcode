class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def dfs(jug1, jug2):
            seen.add((jug1, jug2))
            
            if jug1 == targetCapacity or jug2 == targetCapacity or jug1 + jug2 == targetCapacity:
                return True
            
            states = [(jug1Capacity, jug2), (jug1, jug2Capacity), (0, jug2), (jug1, 0), (jug1 - min(jug1, jug2Capacity - jug2), jug2 + min(jug1, jug2Capacity - jug2)), (jug1 + min(jug2, jug1Capacity - jug1), jug2 - min(jug2, jug1Capacity - jug1))]
            
            for j1, j2 in states:
                if (j1, j2) not in seen:
                    seen.add((j1, j2))
                    if dfs(j1, j2):
                        return True
            
            return False
        
        if targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0:
            seen = set()
            return dfs(0, 0)
        
        return False