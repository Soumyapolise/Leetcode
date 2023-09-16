import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(threshold):
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True
            min_heap = [(0, 0, 0)]  # (effort, row, col)

            while min_heap:
                effort, row, col = heapq.heappop(min_heap)

                if row == rows - 1 and col == cols - 1:
                    return True

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                        new_effort = max(effort, abs(heights[row][col] - heights[r][c]))
                        if new_effort <= threshold:
                            visited[r][c] = True
                            heapq.heappush(min_heap, (new_effort, r, c))

            return False

        left, right = 0, int(1e6)

        while left < right:
            mid = (left + right) // 2
            if bfs(mid):
                right = mid
            else:
                left = mid + 1

        return left