class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adjList[manager[i]].append(i)
        
        return self.dfs(headID, informTime, adjList)
        
    def dfs(self, manager, informTime, adjList):
        maxTime = 0
        for subordinate in adjList[manager]:
            maxTime = max(maxTime, self.dfs(subordinate, informTime, adjList))
        return maxTime + informTime[manager]
        
    
        #   0
        # / | | \
        # 2 5 6 7
        #   | | |
        #   1 3 4
        
        
        
        