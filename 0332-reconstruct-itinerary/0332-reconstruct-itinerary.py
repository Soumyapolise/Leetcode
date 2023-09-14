class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = {}
        
        for source, destination in sorted(tickets)[::-1]:
            if source not in d:
                d[source] = []
            d[source] += [destination]
        
        res = []
        def dfs(city):
            if city in d: 
                while d[city]:
                    dfs(d[city].pop())
            res.append(city)
            
        
        dfs("JFK")
        return res[::-1]
    