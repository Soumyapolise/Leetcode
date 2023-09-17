class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
    
        # Initialize a 2D array dp with dimensions (1 << n) x n
        dp = [[float('inf')] * n for _ in range(1 << n)]

        # Initialize the queue with initial state (node, bitmask, distance)
        queue = [(i, 1 << i, 0) for i in range(n)]

        # Mark the starting nodes as visited with distance 0
        for i in range(n):
            dp[1 << i][i] = 0

        while queue:
            node, mask, distance = queue.pop(0)

            if mask == (1 << n) - 1:
                return distance

            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)

                if dp[new_mask][neighbor] > distance + 1:
                    dp[new_mask][neighbor] = distance + 1
                    queue.append((neighbor, new_mask, distance + 1))
                