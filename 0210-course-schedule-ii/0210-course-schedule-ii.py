class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        print(graph)

        # Initialize the visited and stack lists
        visited = [0] * numCourses  # 0 represents not visited, 1 represents visiting, 2 represents visited
        stack = []

        def dfs(node):
            # Return False if a cycle is detected
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 2
            stack.append(node)
            return True

        # Visit all courses
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []

        # The stack contains the topological ordering of courses
        return stack
