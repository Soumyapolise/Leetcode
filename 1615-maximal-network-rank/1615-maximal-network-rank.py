class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        res = 0
        if roads == []:
            return 0
        
        # Create an adjacency list to represent the connections between cities
        adjacency_list = [[] for _ in range(n)]
        for road in roads:
            adjacency_list[road[0]].append(road[1])
            adjacency_list[road[1]].append(road[0])

        # Calculate the network rank for each pair of cities
        for i in range(n-1):
            for j in range(i+1, n):
                count = len(adjacency_list[i]) + len(adjacency_list[j])
                
                if j in adjacency_list[i]:
                    count -= 1
                res = max(res, count)
        
        return res


# class Solution:
#     def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
#         res = 0
#         if roads == []:
#             return 0
        
#         def dfs(i, j, roads, visited, count):
#             for road in roads:
                
#                 if i in road and road not in visited:
#                     count += 1
#                     visited.append(road)

#                 if j in road and road not in visited:
#                     count += 1
#                     visited.append(road)
#             # print(road, i, j, visited, count)
#             if road == roads[-1]:
#                 return count
        
#         for i in range(n-1):
#             for j in range(i, n):
#                 visited = []
#                 count = 0
#                 count = dfs(i, j, roads, visited, count)
#                 # print(i, count)
#                 res = max(res, count)
        
#         return res
            