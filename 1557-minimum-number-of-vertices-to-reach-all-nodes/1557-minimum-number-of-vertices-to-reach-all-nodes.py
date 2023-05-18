class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = set()
        
        for a, b in edges:
            indegrees.add(b)
            
        return [x for x in range(n) if x not in indegrees]