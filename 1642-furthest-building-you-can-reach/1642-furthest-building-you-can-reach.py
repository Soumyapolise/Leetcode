class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i-1]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap) #popping the minimum height diff to use bricks cuz HEAP internally sorts stuff, not in a physical way though fyi.
                if bricks < 0:
                    return i - 1
        
        return len(heights) - 1