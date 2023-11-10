class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        if n == 2:
            return adjacentPairs[0]
        
        d = {}
        
        for a, b in adjacentPairs:
            if a not in d:
                d[a] = []
            if b not in d:
                d[b] = []
            d[a].append(b)
            d[b].append(a)

        # Find the initial key (a node with only one neighbor)
        start = None
        for key, val in d.items():
            if len(val) == 1:
                start = key
                break

        res = [start]
        visited = set([start])

        # Reconstruct the array
        while len(res) < n:
            current = res[-1]
            for neighbor in d[current]:
                if neighbor not in visited:
                    res.append(neighbor)
                    visited.add(neighbor)
                    break

        return res