class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1]*(n+1)
        for i in range(n):
            if col[i] == -1:
                if not self.dfs(i, 0, col, graph):
                    return False
        return True
    
    def dfs(self, i, c, col, graph) -> bool:
        col[i] = c
        for child in graph[i]:
            if col[child] == -1:
                if not self.dfs(child, 1-c, col, graph):
                    return False
            elif col[i] == col[child]:
                return False
        
        return True
        