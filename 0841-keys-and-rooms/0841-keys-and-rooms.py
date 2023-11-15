class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        res = set()
        n = len(rooms)
        visited = set()
        
        def dfs(room):
            if room in visited:
                return
            
            res.add(room)
            visited.add(room)
            
            for r in rooms[room]:
                dfs(r)
            
        dfs(0)
        return len(res) == n
        