class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        queue = deque()
        queue.append([0, 0, 1])
        dx = [-1,0,1]
        dy = [-1,0,1]
        grid[0][0] = 1
        
        while queue:
            x, y, steps = queue.popleft()
            if x == n-1 and y == n-1:
                return steps
            
            for i in range(3):
                for j in range(3):
                    nx = x + dx[i]
                    ny = y + dy[j]
                    
                    if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny] == 0:
                        queue.append([nx, ny, steps+1])
                        grid[nx][ny] = 1
                        
        return -1
            