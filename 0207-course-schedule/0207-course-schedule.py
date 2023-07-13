class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for c, p in prerequisites:
            courses[p].append(c)
        print(courses)
        seen = set()

        def check_cycle(cur, path):
            if cur in path:
                return True
            if cur in seen:
                return False

            path.add(cur)
            for child in courses[cur]:
                if check_cycle(child, path):
                    return True
            path.remove(cur)

            seen.add(cur)

            return False

        for cur in range(numCourses):
            if check_cycle(cur, set()):
                return False

        return True