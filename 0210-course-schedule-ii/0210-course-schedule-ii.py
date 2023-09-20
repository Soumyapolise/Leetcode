class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites:
            graph[course] += [prereq]
        
        visited = [0 for _ in range(numCourses)]
        res = []
        
        def dfs(course):
            if visited[course] == 1:
                return False
            
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for c in graph[course]:
                if not dfs(c):
                    return False
            
            visited[course] = 2
            res.append(course)
            return True
        
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return []
            
        return res