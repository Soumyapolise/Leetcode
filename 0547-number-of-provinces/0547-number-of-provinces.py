from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        visited = [False]*n
        
        def dfs(node):
            visited[node] = True
            for neighbour in range(n):
                if isConnected[node][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)
        
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)
        
        return provinces
