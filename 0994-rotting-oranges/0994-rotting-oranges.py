class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==  2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]       
        res = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in dirs:
                    if 0 <= x + dx < m and 0 <= y + dy < n and grid[x+dx][y+dy] == 1:
                        q.append((x+dx, y+dy))
                        grid[x+dx][y+dy] = 2
                        fresh -= 1
            
            res += 1
        
        if fresh != 0:
            return -1
        
        return max(res-1, 0)
                